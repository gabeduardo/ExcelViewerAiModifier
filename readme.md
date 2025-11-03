
---


This project allows users to upload an Excel file, enrich its data using a Language Model (LLM), and download the modified version. It includes a FastAPI backend and a Next.js + TypeScript frontend, fully containerized with Docker.

---

##  Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/excel-ai-modifier.git
cd excel-ai-modifier
```

### 2. Configure the LLM API key

Inside the `backend/app` folder, rename the environment file:

```
.env.dist  to .env
```


---

### 3. Build and start the project

From the root of the project, run:

```bash
docker-compose up --build
```

This will build and launch both the backend and frontend services.

---

### 4. Use the application

- Open your browser and go to: [http://localhost:3000](http://localhost:3000)
- Upload your Excel file
- Wait for the sheet to load
- Click **Export / Modify File** to download the enriched version

---
