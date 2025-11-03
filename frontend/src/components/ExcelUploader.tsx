import React from "react";

type Props = {
  onFileLoaded: (file: File, sheetNames: string[]) => void;
};

const ExcelUploader: React.FC<Props> = ({ onFileLoaded }) => {
  const handleUpload = async (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (!file) return;

    const formData = new FormData();
    formData.append("file", file);

    const res = await fetch(`http://localhost:8001/upload`, {
      method: "POST",
      body: formData,
    });

    const data = await res.json();
    onFileLoaded(file, data.sheets);
  };

  return <input type="file" accept=".xlsx" onChange={handleUpload} />;
};

export default ExcelUploader;