import fs from "fs/promises"
import { Document, VectorStoreIndex } from "llamaindex"

async function main() {
    const essay = await fs.readFile(
        './paul_graham_essay.txt',
        'utf-8',
    );
    const document = new Document({ text: essay });
    
    const index = await VectorStoreIndex.fromDocuments([document])
    const queryEngine = index.asQueryEngine();

    const response = await queryEngine.query(
        "What is the author's favorite hobby?",
    );
    console.log(response.toString());
}

main();