import os
import psycopg
from dotenv import load_dotenv

load_dotenv()


class PostgreSQLService:

    def __init__(self):

        host = os.getenv("POSTGRES_HOST", "localhost")
        port = int(os.getenv("POSTGRES_PORT", "5432"))
        dbname = os.getenv("POSTGRES_DB", "pms")
        user = os.getenv("POSTGRES_USER", "postgres")
        password = os.getenv("POSTGRES_PASSWORD", "root")
        schema = os.getenv("POSTGRES_SCHEMA", "pms_vector")

        self.connection = psycopg.connect(
            host=host,
            port=port,
            dbname=dbname,
            user=user,
            password=password,
            options=f"-c search_path={schema},public"
        )

        self.cursor = self.connection.cursor()

        print(f"Connected to PostgreSQL on {host}:{port}/{dbname} (schema: {schema}).")

    def save_document(self, document):

        self.cursor.execute(
            """
            INSERT INTO documents (
                document_id,
                document_name,
                document_type,
                document_hash,
                title,
                language,
                file_size,
                page_count,
                character_count,
                word_count,
                access_scope,
                created_at
            )
            VALUES (
                %s, %s, %s, %s, %s, %s,
                %s, %s, %s, %s, %s, %s
            )
            """,
            (
                document["document_id"],
                document["document_name"],
                document["document_type"],
                document["metadata"]["document_hash"],
                document["metadata"]["title"],
                document["language"],
                document["metadata"]["file_size"],
                document["page_count"],
                document["metadata"]["character_count"],
                document["metadata"]["word_count"],
                document["access_scope"],
                document["metadata"]["created_at"],
            )
        )

        self.connection.commit()

        print("Document saved successfully.")

    def save_chunks(self, chunks):

        for chunk in chunks:

            child_text = chunk.get("child_text") or chunk.get("text", "")
            parent_text = chunk.get("parent_text") or child_text
            doc_name = chunk.get("doc_name") or chunk.get("document_name", "")
            folder_path = chunk.get("folder_path", "")
            heading = chunk.get("heading") or "Untitled"
            language = chunk.get("language") or "en"

            self.cursor.execute(
                """
                INSERT INTO chunks (
                    chunk_id,
                    doc_name,
                    folder_path,
                    page_number,
                    heading,
                    language,
                    parent_text,
                    child_text,
                    embedding,
                    tsv
                )
                VALUES (
                    %s, %s, %s, %s,
                    %s, %s, %s, %s,
                    %s, to_tsvector('english', %s)
                )
                """,
                (
                    chunk["chunk_id"],
                    doc_name,
                    folder_path,
                    chunk["page_number"],
                    heading,
                    language,
                    parent_text,
                    child_text,
                    chunk["embedding"],
                    child_text,
                )
            )

        self.connection.commit()

        print(f"{len(chunks)} chunks saved successfully.")

    def search_similar_chunks(self, query_embedding, top_k=5):

        self.cursor.execute(
            """
            SELECT
                chunk_id,
                doc_name,
                folder_path,
                page_number,
                heading,
                language,
                parent_text,
                child_text,
                embedding <=> %s::vector AS distance
            FROM chunks
            ORDER BY embedding <=> %s::vector
            LIMIT %s;
            """,
            (
                query_embedding,
                query_embedding,
                top_k,
            )
        )
    
        rows = self.cursor.fetchall()
    
        results = []
    
        for row in rows:
        
            results.append(
                {
                    "chunk_id": row[0],
                    "doc_name": row[1],
                    "folder_path": row[2],
                    "page_number": row[3],
                    "heading": row[4],
                    "language": row[5],
                    "parent_text": row[6],
                    "child_text": row[7],
                    "text": row[7],  # Backwards compatibility
                    "distance": row[8],
                }
            )
    
        return results

    def close(self):

        self.cursor.close()
        self.connection.close()

        print("Connection Closed.")