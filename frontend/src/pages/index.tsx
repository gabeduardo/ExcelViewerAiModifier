import { useState } from "react";

import ExcelUploader from "../components/ExcelUploader";
import SheetTabs from "../components/SheetTabs";
import SheetTable from "../components/SheetTable";
import ExportButton from "../components/ExportButton";

export default function Home() {
  const [file, setFile] = useState<File | null>(null);
  const [sheets, setSheets] = useState<string[]>([]);
  const [selectedSheet, setSelectedSheet] = useState<string>("");
  const [sheetData, setSheetData] = useState<any[][]>([]);

  return (
    <main style={{ padding: "2rem" }}>
      <h1>Excel Viewer & Modifier</h1>
      <ExcelUploader
        onFileLoaded={(f, sheetNames) => {
          setFile(f);
          setSheets(sheetNames);
          setSelectedSheet(sheetNames[0]);
        }}
      />
      {sheets.length > 0 && (
        <>
          <SheetTabs
            sheets={sheets}
            selected={selectedSheet}
            onSelect={setSelectedSheet}
          />
          <SheetTable
            file={file}
            sheet={selectedSheet}
            onDataLoaded={setSheetData}
          />
          <ExportButton file={file} sheet={selectedSheet} />
        </>
      )}
    </main>
  );
}