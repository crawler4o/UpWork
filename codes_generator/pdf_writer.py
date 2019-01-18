from fpdf import FPDF
import sqlite3
import time


def write_codes(codes_it, name):
    pdf = FPDF('P', 'mm', (330, 480))
    pdf.add_font('Calibri', '', 'calibri.ttf', uni=True)
    pdf.set_author('Asen Georgiev')
    pdf.add_page()
    pdf.set_font('Calibri', '', 12)  # B,I or U on the second position
    pdf.set_auto_page_break(False)  # Not to add a new page when the cursor goes too low
    small_step = True
    x_ofs = 0
    y_ofs = 0
    pdf.ln(41)  # header on the first page
    pdf.cell(20)  # margin on the first page
    for code in codes_it:
        pdf.cell(20, 10, code, 0, 0, 'C')

        if x_ofs < 5:  # if the line is not full
            pdf.cell(30)  # right shifting in mm
            x_ofs += 1
        elif x_ofs == 5:  # if the line is full
            if small_step:
                pdf.ln(24)  # the small line shift in mm
                small_step = False
                pdf.rotate(180)  # turning the letters upside down
                pdf.cell(-290)  # shifting one full line because flipped line starts from the right
            else:
                pdf.ln(94)  # the big line shift in mm
                pdf.rotate(0)  # restoring the flipped letters
                pdf.cell(20)
                small_step = True

            if y_ofs < 7:  # if the page is not full
                y_ofs += 1
            else:  # if the page is full
                y_ofs = 0
                if pdf.page_no() < 1042:  # not to have an empty page in the end
                    pdf.add_page()
                    pdf.ln(41)  # header
                    pdf.cell(20)  # margin

            x_ofs = 0
    pdf.output(name, 'F')


def query_codes(amount, file_name):

    conn = sqlite3.connect('chio_codes.sqlite')
    cur = conn.cursor()
    time_now = time.strftime('%Y-%m-%d %H:%M:%S')

    cur.execute('''INSERT OR IGNORE INTO Usage (datetime, pdf_file_name)
        VALUES (?, ?)''', (time_now, file_name))
    cur.execute('SELECT id FROM Usage WHERE datetime = ? ', (time_now, ))
    usage_id = cur.fetchone()[0]

    cur.execute('UPDATE Codes SET usage_id = ? WHERE id in (SELECT id FROM Codes WHERE usage_id IS NULL LIMIT ?)',
                (usage_id, amount))

    cur.execute('SELECT code FROM Codes WHERE usage_id = ? ', (usage_id, ))
    codes_it = cur.fetchall()
    conn.commit()
    return (code[0] for code in codes_it)


if __name__ == '__main__':
    for _ in range(102):
        out_file = 'Chio_Codes_{}.pdf'.format(time.strftime('%Y_%m_%d_%H_%M_%S'))
        codes = query_codes(50016, out_file)  # 50016 codes per file, 1042 pages
        write_codes(codes, out_file)
