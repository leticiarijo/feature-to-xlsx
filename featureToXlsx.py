import os
import xlsxwriter

def parse_feature_file(file_path):
    scenarios, current, in_expected = [], None, False
    with open(file_path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line.startswith("Cenário:"):
                if current: scenarios.append(current)
                current = {"title": line.replace("Cenário:", "").strip(), "steps": [], "expected": []}
                in_expected = False
            elif line.startswith(("Então","Entao")):
                current["expected"].append(line); in_expected = True
            elif line.startswith("E") and in_expected:
                current["expected"].append(line)
            elif line.startswith(("Dado","Quando")) or (line.startswith("E") and not in_expected):
                current["steps"].append(line)
    if current: scenarios.append(current)
    return scenarios

def write_to_excel(scenarios, output_file):
    wb, ws = xlsxwriter.Workbook(output_file), None
    ws = wb.add_worksheet()
    headers = ["Work Item Type","Title","Test Step","Step Action","Step Expected"]
    for col, h in enumerate(headers): ws.write(0, col, h)

    row = 1
    for sc in scenarios:
        ws.write_row(row, 0, ["Test Case", sc["title"], "", "", ""]); row += 1
        step = 1
        for s in sc["steps"]:
            ws.write_row(row, 0, ["","", step, s, ""]); row += 1; step += 1
        for e in sc["expected"]:
            ws.write_row(row, 0, ["","", step, "", e]); row += 1; step += 1
    wb.close()

def process_all_features(directory="."):
    for f in os.listdir(directory):
        if f.endswith(".feature"):
            try:
                xlsx = os.path.splitext(f)[0] + ".xlsx"
                scenarios = parse_feature_file(f)
                write_to_excel(scenarios, xlsx)
                print(f"✅ Gerado: {xlsx}")
            except Exception as e:
                print(f"❌ Erro ao processar {f}: {e}")

if __name__ == "__main__":
    process_all_features(".")
