type Props = {
  sheets: string[];
  selected: string;
  onSelect: (sheet: string) => void;
};

const SheetTabs: React.FC<Props> = ({ sheets, selected, onSelect }) => {
  return (
    <div style={{ display: "flex", gap: "1rem", marginTop: "1rem" }}>
      {sheets.map((sheet) => (
        <button
          key={sheet}
          onClick={() => onSelect(sheet)}
          style={{
            background: sheet === selected ? "#0070f3" : "#eee",
            color: sheet === selected ? "#fff" : "#000",
            padding: "0.5rem 1rem",
            borderRadius: "4px",
          }}
        >
          {sheet}
        </button>
      ))}
    </div>
  );
};

export default SheetTabs;