import xml.etree.ElementTree as ET


def create_rounded_rect(parent, x, y, width, height, r, fill, stroke, stroke_width, label, sublabel=""):
    g = ET.SubElement(parent, "g")
    rect = ET.SubElement(g, "rect")
    rect.set("x", str(x))
    rect.set("y", str(y))
    rect.set("width", str(width))
    rect.set("height", str(height))
    rect.set("rx", str(r))
    rect.set("ry", str(r))
    rect.set("fill", fill)
    rect.set("stroke", stroke)
    rect.set("stroke-width", str(stroke_width))

    text_x = x + width / 2
    text_y = y + height / 2

    if sublabel:
        text_y -= 5

    text = ET.SubElement(g, "text")
    text.set("x", str(text_x))
    text.set("y", str(text_y + 5))
    text.set("text-anchor", "middle")
    text.set("font-family", "Arial, sans-serif")
    text.set("font-size", "14")
    text.set("fill", "#333")
    text.text = label

    if sublabel:
        subtext = ET.SubElement(g, "text")
        subtext.set("x", str(text_x))
        subtext.set("y", str(text_y + 20))
        subtext.set("text-anchor", "middle")
        subtext.set("font-family", "Arial, sans-serif")
        subtext.set("font-size", "10")
        subtext.set("fill", "#666")
        subtext.text = sublabel

    return g


def create_arrow(parent, x1, y1, x2, y2, color="#333"):
    path = ET.SubElement(parent, "path")
    d = f"M {x1} {y1} L {x2} {y2}"
    path.set("d", d)
    path.set("stroke", color)
    path.set("stroke-width", "2")
    path.set("marker-end", "url(#arrowhead)")


def create_elbow_arrow(parent, x1, y1, x2, y2, elbow_x, color="#333"):
    path = ET.SubElement(parent, "path")
    d = f"M {x1} {y1} L {elbow_x} {y1} L {elbow_x} {y2} L {x2} {y2}"
    path.set("d", d)
    path.set("stroke", color)
    path.set("stroke-width", "2")
    path.set("fill", "none")
    path.set("marker-end", "url(#arrowhead)")


def main():
    svg = ET.Element("svg")
    svg.set("xmlns", "http://www.w3.org/2000/svg")
    svg.set("width", "1200")
    svg.set("height", "1400")
    svg.set("viewBox", "0 0 1200 1400")

    # Definitions
    defs = ET.SubElement(svg, "defs")
    marker = ET.SubElement(defs, "marker")
    marker.set("id", "arrowhead")
    marker.set("markerWidth", "10")
    marker.set("markerHeight", "7")
    marker.set("refX", "9")
    marker.set("refY", "3.5")
    marker.set("orient", "auto")
    polygon = ET.SubElement(marker, "polygon")
    polygon.set("points", "0 0, 10 3.5, 0 7")
    polygon.set("fill", "#333")

    # Styles
    style_dino = {"fill": "#e1f5fe", "stroke": "#0277bd"}
    style_conv = {"fill": "#fff3e0", "stroke": "#ef6c00"}
    style_block = {"fill": "#f3e5f5", "stroke": "#7b1fa2"}
    style_head = {"fill": "#e8f5e9", "stroke": "#2e7d32"}
    style_detect = {"fill": "#ffebee", "stroke": "#c62828"}
    style_input = {"fill": "#f5f5f5", "stroke": "#333"}

    # Layout Configuration
    center_x = 300  # Shifted right
    head_x = 700  # Shifted right
    start_y = 50
    gap_y = 80  # Increased vertical gap slightly
    box_w = 200  # Slightly wider boxes
    box_h = 60

    # --- Backbone (Left Column) ---

    # Input
    y = start_y
    create_rounded_rect(
        svg, center_x - box_w / 2, y, box_w, box_h, 10, **style_input, stroke_width=2, label="Input Image"
    )
    prev_y = y + box_h

    # P0 DINO
    y += gap_y
    create_rounded_rect(
        svg,
        center_x - box_w / 2,
        y,
        box_w,
        box_h,
        5,
        **style_dino,
        stroke_width=2,
        label="DINO3Preprocessor",
        sublabel="P0 Input",
    )
    create_arrow(svg, center_x, prev_y, center_x, y)
    prev_y = y + box_h

    # P1 Conv
    y += gap_y
    create_rounded_rect(
        svg, center_x - box_w / 2, y, box_w, box_h, 5, **style_conv, stroke_width=2, label="Conv", sublabel="P1/2"
    )
    create_arrow(svg, center_x, prev_y, center_x, y)
    prev_y = y + box_h

    # P2 Conv
    y += gap_y
    create_rounded_rect(
        svg, center_x - box_w / 2, y, box_w, box_h, 5, **style_conv, stroke_width=2, label="Conv", sublabel="P2/4"
    )
    create_arrow(svg, center_x, prev_y, center_x, y)
    prev_y = y + box_h

    # P2 C3k2
    y += gap_y
    create_rounded_rect(
        svg, center_x - box_w / 2, y, box_w, box_h, 5, **style_block, stroke_width=2, label="C3k2", sublabel="P2"
    )
    create_arrow(svg, center_x, prev_y, center_x, y)
    prev_y = y + box_h

    # P3 Conv
    y += gap_y
    create_rounded_rect(
        svg, center_x - box_w / 2, y, box_w, box_h, 5, **style_conv, stroke_width=2, label="Conv", sublabel="P3/8"
    )
    create_arrow(svg, center_x, prev_y, center_x, y)
    prev_y = y + box_h

    # P3 C3k2
    y += gap_y
    create_rounded_rect(
        svg,
        center_x - box_w / 2,
        y,
        box_w,
        box_h,
        5,
        **style_block,
        stroke_width=2,
        label="C3k2",
        sublabel="Standard P3",
    )
    create_arrow(svg, center_x, prev_y, center_x, y)
    prev_y = y + box_h

    # P3 DINO
    y += gap_y
    create_rounded_rect(
        svg,
        center_x - box_w / 2,
        y,
        box_w,
        box_h,
        5,
        **style_dino,
        stroke_width=2,
        label="DINO3Backbone",
        sublabel="Enhanced P3",
    )
    create_arrow(svg, center_x, prev_y, center_x, y)
    prev_y = y + box_h
    p3_dino_y = y + box_h / 2  # Save P3 DINO center Y

    # P4 Conv
    y += gap_y
    create_rounded_rect(
        svg, center_x - box_w / 2, y, box_w, box_h, 5, **style_conv, stroke_width=2, label="Conv", sublabel="P4/16"
    )
    create_arrow(svg, center_x, prev_y, center_x, y)
    prev_y = y + box_h

    # P4 A2C2f
    y += gap_y
    create_rounded_rect(
        svg,
        center_x - box_w / 2,
        y,
        box_w,
        box_h,
        5,
        **style_block,
        stroke_width=2,
        label="A2C2f",
        sublabel="Standard P4",
    )
    create_arrow(svg, center_x, prev_y, center_x, y)
    prev_y = y + box_h
    p4_y = y + box_h / 2  # Save P4 center Y

    # P5 Conv
    y += gap_y
    create_rounded_rect(
        svg, center_x - box_w / 2, y, box_w, box_h, 5, **style_conv, stroke_width=2, label="Conv", sublabel="P5/32"
    )
    create_arrow(svg, center_x, prev_y, center_x, y)
    prev_y = y + box_h

    # P5 A2C2f
    y += gap_y
    create_rounded_rect(
        svg,
        center_x - box_w / 2,
        y,
        box_w,
        box_h,
        5,
        **style_block,
        stroke_width=2,
        label="A2C2f",
        sublabel="Standard P5",
    )
    create_arrow(svg, center_x, prev_y, center_x, y)
    prev_y = y + box_h
    p5_y = y + box_h / 2  # Save P5 center Y

    # --- Head (Right Column) ---
    # Align Head blocks roughly with their Backbone counterparts or slightly offset

    # Path 1: P5 -> P4
    # Upsample P5
    h_y = p5_y
    # Concat with P4
    h_y = p4_y
    create_rounded_rect(
        svg, head_x - box_w / 2, h_y, box_w, box_h, 5, **style_head, stroke_width=2, label="A2C2f", sublabel="Head P4"
    )
    # Arrow from P5 (up and over)
    create_elbow_arrow(svg, center_x + box_w / 2, p5_y, head_x, h_y - box_h / 2, head_x + 50)  # Simplified connection
    # Arrow from P4
    create_arrow(svg, center_x + box_w / 2, p4_y, head_x - box_w / 2, h_y)
    head_p4_y = h_y

    # Path 2: P4 -> P3
    h_y = p3_dino_y  # Align with P3 DINO
    create_rounded_rect(
        svg,
        head_x - box_w / 2,
        h_y,
        box_w,
        box_h,
        5,
        **style_head,
        stroke_width=2,
        label="A2C2f",
        sublabel="Head P3 (Small)",
    )
    # Arrow from Head P4 (down)
    create_arrow(svg, head_x, head_p4_y + box_h / 2, head_x, h_y - box_h / 2)
    # Arrow from P3 DINO
    create_arrow(svg, center_x + box_w / 2, p3_dino_y, head_x - box_w / 2, h_y)
    head_p3_y = h_y

    # Path 3: P3 -> P4 (Output)
    h_y = head_p4_y + 150  # Shift down below Head P4
    create_rounded_rect(
        svg,
        head_x + 200,
        h_y,
        box_w,
        box_h,
        5,
        **style_head,
        stroke_width=2,
        label="A2C2f",
        sublabel="Head P4 (Medium)",
    )
    # Arrow from Head P3
    create_elbow_arrow(svg, head_x + box_w / 2, head_p3_y, head_x + 200, h_y, head_x + 150)
    # Arrow from Head P4 (skip connection/concat)
    create_elbow_arrow(svg, head_x + box_w / 2, head_p4_y + box_h / 2, head_x + 200, h_y + box_h / 2, head_x + 150)

    head_p4_out_y = h_y
    head_p4_out_x = head_x + 200

    # Path 4: P4 -> P5 (Output)
    h_y = head_p4_out_y + 100
    create_rounded_rect(
        svg, head_x + 200, h_y, box_w, box_h, 5, **style_head, stroke_width=2, label="C3k2", sublabel="Head P5 (Large)"
    )
    # Arrow from Head P4 Out
    create_arrow(svg, head_p4_out_x + box_w / 2, head_p4_out_y + box_h, head_p4_out_x + box_w / 2, h_y)
    # Arrow from Backbone P5
    create_elbow_arrow(svg, center_x + box_w / 2, p5_y, head_x + 200, h_y + box_h / 2, center_x + 100)

    head_p5_out_y = h_y
    head_p5_out_x = head_x + 200

    # --- Detect ---
    detect_y = head_p5_out_y + 120
    # Center Detect block relative to the whole diagram width roughly
    detect_x = (center_x + head_x + 200) / 2
    create_rounded_rect(
        svg,
        detect_x - (box_w * 2.5) / 2,
        detect_y,
        box_w * 2.5,
        box_h,
        5,
        **style_detect,
        stroke_width=2,
        label="Detect",
        sublabel="P3, P4, P5",
    )

    # Connections to Detect
    # Target point on Detect block
    detect_target_x = detect_x
    detect_target_y = detect_y

    # From P3 (Head P3)
    create_elbow_arrow(
        svg, head_x - box_w / 2, head_p3_y + box_h / 2, detect_target_x - 100, detect_target_y, head_x - box_w / 2
    )
    # From P4 (Head P4 Out)
    create_elbow_arrow(
        svg,
        head_p4_out_x + box_w / 2,
        head_p4_out_y + box_h,
        detect_target_x,
        detect_target_y,
        head_p4_out_x + box_w / 2,
    )
    # From P5 (Head P5 Out)
    create_elbow_arrow(
        svg,
        head_p5_out_x + box_w / 2,
        head_p5_out_y + box_h,
        detect_target_x + 100,
        detect_target_y,
        head_p5_out_x + box_w / 2,
    )

    tree = ET.ElementTree(svg)
    tree.write("dinov3_yolov12_dualp0p3.svg")
    print("SVG generated: dinov3_yolov12_dualp0p3.svg")


if __name__ == "__main__":
    main()
