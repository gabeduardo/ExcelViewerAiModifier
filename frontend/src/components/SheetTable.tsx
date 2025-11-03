import { useEffect, useState } from "react";
import * as XLSX from "xlsx";

type Props = {
  file: File | null;
  sheet: string;
  onDataLoaded: (data: any[][]) => void;
};

const SheetTable: React.FC<Props> = ({ file, sheet, onDataLoaded }) => {
  const [data, setData] = useState<any[][]>([]);

  useEffect(() => {
    if (!file || !sheet) return;

    const reader = new FileReader();
    reader.onload = (e) => {
      const bytes = new Uint8Array(e.target?.result as ArrayBuffer);
      const workbook = XLSX.read(bytes, { type: "array" });
      const ws = workbook.Sheets[sheet];
      const rows = XLSX.utils.sheet_to_json(ws, { header: 1 });
      setData(rows as any[][]);
      onDataLoaded(rows as any[][]);
    };
    reader.readAsArrayBuffer(file);
  }, [file, sheet]);

  if (!data || data.length === 0) return null;

  return (
    <table style={{ marginTop: "1rem", borderCollapse: "collapse", width: "100%" }}>
      <thead>
        <tr>
          {data[0].map((cell, i) => (
            <th key={i} style={{ border: "1px solid #ccc", padding: "0.5rem", background: "#f0f0f0" }}>
              {cell}
            </th>
          ))}
        </tr>
      </thead>
      <tbody>
        {data.slice(1).map((row, rowIndex) => (
          <tr key={rowIndex}>
            {row.map((cell, colIndex) => (
              <td key={colIndex} style={{ border: "1px solid #ccc", padding: "0.5rem" }}>
                {cell}
              </td>
            ))}
          </tr>
        ))}
      </tbody>
    </table>
  );
};

export default SheetTable;