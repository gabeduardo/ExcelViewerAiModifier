import { useEffect } from "react";
import * as XLSX from "xlsx";

type Props = {
  file: File | null;
  sheet: string;
  onDataLoaded: (data: any[][]) => void;
};

const SheetTable: React.FC<Props> = ({ file, sheet, onDataLoaded }) => {
  useEffect(() => {
    if (!file || !sheet) return;

    const reader = new FileReader();
    reader.onload = (e) => {
      const data = new Uint8Array(e.target?.result as ArrayBuffer);
      const workbook = XLSX.read(data, { type: "array" });
      const ws = workbook.Sheets[sheet];
      const rows = XLSX.utils.sheet_to_json(ws, { header: 1 });
      onDataLoaded(rows as any[][]);
    };
    reader.readAsArrayBuffer(file);
  }, [file, sheet]);

  return null; // Solo carga datos, no renderiza tabla directamente
};

export default SheetTable;