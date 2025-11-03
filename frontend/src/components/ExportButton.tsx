type Props = {
  file: File | null;
  sheet: string;
};

const ExportButton: React.FC<Props> = ({ file, sheet }) => {
  const handleExport = async () => {
    if (!file || !sheet) {
      console.warn("❌ Exportación cancelada: archivo o hoja no definidos");
      return;
    }

    console.log("🛠️ Exportando hoja:", sheet);
    console.log("🛠️ Archivo:", file.name);
    console.log("🛠️ Enviando a:", "http://localhost:8001/modify");

    const formData = new FormData();
    formData.append("file", file);
    formData.append("sheet", sheet);

    try {
      const res = await fetch(`http://localhost:8001/modify`, {
        method: "POST",
        body: formData,
      });

      if (!res.ok) {
        throw new Error(`Error ${res.status}`);
      }

      const blob = await res.blob();
      console.log("✅ Archivo modificado recibido, iniciando descarga");

      const url = URL.createObjectURL(blob);
      const a = document.createElement("a");
      a.href = url;
      a.download = "modified.xlsx";
      a.click();
    } catch (error) {
      console.error("❌ Error al modificar el archivo:", error);
    }
  };

  return (
    <button onClick={handleExport} style={{ marginTop: "2rem" }}>
      Export Modified Excel
    </button>
  );
};

export default ExportButton;