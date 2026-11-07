import google.generativeai as genai
from sympy.abc import x, y, z, t
import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QMessageBox
)
from pdf2image import convert_from_path
from math import degrees
import openpyxl
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font
from openpyxl.utils import get_column_letter
from sympy import simplify, collect
from itertools import combinations
import itertools
from PyQt5.QtCore import QSettings
import sys
import os
import platform
import subprocess
import hashlib
import time
from datetime import datetime, timedelta
# Bổ sung các widget và core cho Splash Screen
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar  # <-- BỔ SUNG 2 CÁI NÀY
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal  # <-- BỔ SUNG QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea  # <-- Thêm mục này vào đây
)
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt, QPropertyAnimation, pyqtProperty
from functools import wraps
import re
import uuid
import json, base64
from datetime import datetime
from nacl.signing import VerifyKey
from nacl.encoding import HexEncoder
from nacl.exceptions import BadSignatureError
### CÔNG CỤ
import sys
import numpy as np
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QDialog, 
    QVBoxLayout, QHBoxLayout, QTabWidget, QWidget, 
    QLabel, QSlider, QDoubleSpinBox, QGroupBox
)
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D  # Cần cho 3D


def bt_dang11_p2_b4_c1_hh11(self):
    # ==================== HÌNH VẼ TIKZ ====================
    # Hình vẽ TikZ chuẩn 100% theo mẫu ảnh
    tikz_fig = ('''\\begin{center}
\\begin{tikzpicture}[scale=0.9, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (B) at (0,0);
\\coordinate (C) at (4.5,-0.6);
\\coordinate (A) at (1.8,1.8);
\\coordinate (D) at ($(C)+(A)-(B)$);
\\coordinate (h) at (-1.4,3.2);
\\coordinate (B1) at ($(B)+(h)$);
\\coordinate (C1) at ($(C)+(h)$);
\\coordinate (A1) at ($(A)+(h)$);
\\coordinate (D1) at ($(D)+(h)$);
\\coordinate (O) at ($(A)!0.5!(C)$);
\\coordinate (O1) at ($(A1)!0.5!(C1)$);
\\coordinate (G1) at ($(A)!0.33333!(C1)$);
\\coordinate (G2) at ($(A)!0.66667!(C1)$);
\\coordinate (H) at ($(A)!0.5!(B)$);
\\coordinate (P) at ($(C1)!0.5!(D)$);
\\coordinate (M) at ($(C)!0.5!(C1)$);
\\coordinate (N) at ($(D)!0.5!(D1)$);
\\draw[line width=1pt] (B)--(C)--(D)--(D1)--(A1)--(B1)--(B) (B1)--(C1)--(D1) (C)--(C1) (C)--(B1) (C)--(D1) (C)--(A1) (B1)--(M)--(N)--(A1) (B1)--(D1) (A1)--(C1);
\\draw[line width=1pt, dashed] (B)--(A)--(D) (A)--(A1) (B)--(D) (A)--(C) (A)--(C1)  (A1)--(B) (A1)--(D) (A1)--(O) (C)--(O1) (B1)--(P) (A1)--(G1);
\\fill (B) circle (1pt) node[below left] {$B$};
\\fill (C) circle (1pt) node[below] {$C$};
\\fill (D) circle (1pt) node[right] {$D$};
\\fill (A) circle (1pt) node[left] {$A$};
\\fill (B1) circle (1pt) node[left] {$B'$};
\\fill (C1) circle (1pt) node[above left] {$C'$};
\\fill (A1) circle (1pt) node[above] {$A'$};
\\fill (D1) circle (1pt) node[above right] {$D'$};
\\fill (O) circle (1pt) node[below] {$O$};
\\fill (O1) circle (1pt) node[above] {$O'$};
\\fill (G1) circle (1pt) node[right] {$G_1$};
\\fill (G2) circle (1pt) node[right] {$G_2$};
\\fill (H) circle (1pt) node[below left] {$H$};
\\fill (P) circle (1pt) node[right] {$P$};
\\fill (M) circle (1pt) node[below left] {$M$};
\\fill (N) circle (1pt) node[right] {$N$};
\\end{tikzpicture}
\\end{center}''')
    
    # Random các hệ số sai cho mệnh đề c và hình sai cho mệnh đề d
    he_so_sai_c = random.choice([2, 3, "\\frac{1}{2}", "\\frac{3}{2}"])
    hinh_sai_d = random.choice(["hình thang cân", "hình chữ nhật", "hình thoi"])
    
    # Nội dung câu hỏi
    noidungcauhoi = ('''Cho hình hộp $ABCD.A'B'C'D'$ có các cạnh $AA', BB', CC', DD'$ song song với nhau.''')
    
    ########################################################################
    # Nhận biết 
    ########################################################################
    
    # Các đáp án
    nb_da_1_d = '\\True $(BDA\') // (B\'D\'C)$'
    nb_da_1_s = '$(BDA\')$ cắt $(B\'D\'C)$'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_nb_1 = [nb_da_1]
    
    # Nội dung lời giải
    loigiai_nb_1 = ('''Ta có $BA'D'C$ là hình bình hành nên $BA' // D'C$. \\\\ Ta có $BB'D'D$ là hình bình hành nên $B'D' // BD$. \\\\ Ta có: $\\begin{cases} BA' // D'C \\\\ BD // B'D' \\\\ BA', BD \\subset (BA'D); BA' \\cap BD = B \\\\ B'D', D'C \\subset (B'D'C); B'D' \\cap D'C = D' \\end{cases} \\Rightarrow (BDA') // (B'D'C)$.''')
    
    # Đưa các lời giải vào danh sách lời giải
    list_nb_2 = [loigiai_nb_1]
    
    # Kết hợp các đáp án và lời giải vào cùng một danh sách
    combined_nb = list(zip(list_nb_1, list_nb_2))
    
    # Xáo trộn danh sách kết hợp
    random.shuffle(combined_nb)
    
    # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ########################################################################
    # Thông hiểu 
    ########################################################################
    
    # Các đáp án
    th_da_1_d = '\\True Đường chéo $AC\'$ đi qua trọng tâm $G_1, G_2$ của tam giác $BDA\'$ và $B\'D\'C$'
    th_da_1_s = 'Đường chéo $AC\'$ không đi qua trọng tâm $G_1, G_2$ của tam giác $BDA\'$ và $B\'D\'C$'
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_th_1 = [th_da_1]
    
    # Nội dung lời giải
    loigiai_th_1 = ('''Trong $(ABCD)$, gọi $O = AC \\cap BD$. \\\\ $\\Rightarrow \\begin{cases} O \\in AC; AC \\subset (ACC'A') \\\\ O \\in BD; BD \\subset (BDA') \\end{cases} \\Rightarrow O \\in (ACC'A') \\cap (BDA')$. \\\\ Mà $A' \\in (ACC'A') \\cap (BDA')$ nên $A'O = (ACC'A') \\cap (BDA')$. \\\\ Trong $(ACC'A')$, gọi $E = A'O \\cap AC'$. \\\\ Ta có $\\frac{A'E}{EO} = \\frac{A'C'}{AO} = 2$ (Thales) $\\Rightarrow E$ trùng với trọng tâm $G_1$ của tam giác $BDA'$. (1) \\\\ Trong $(A'B'C'D')$, gọi $O' = A'C' \\cap B'D'$. \\\\ $\\Rightarrow \\begin{cases} O' \\in A'C'; A'C' \\subset (ACC'A') \\\\ O' \\in B'D'; B'D' \\subset (B'D'C) \\end{cases} \\Rightarrow O' \\in (ACC'A') \\cap (B'D'C)$. \\\\ Mà $C \\in (ACC'A') \\cap (B'D'C)$ nên $CO' = (ACC'A') \\cap (B'D'C)$. \\\\ Trong $(ACC'A')$, gọi $F = CO' \\cap AC'$. \\\\ Ta có $\\frac{CF}{FO'} = \\frac{AC}{C'O'} = 2$ (Thales) $\\Rightarrow F$ trùng với trọng tâm $G_2$ của tam giác $B'D'C$. (2) \\\\ Từ (1) và (2) suy ra $AC'$ qua trọng tâm $G_1, G_2$ của tam giác $BDA'$ và $B'D'C$.''')
    
    # Đưa các lời giải vào danh sách lời giải
    list_th_2 = [loigiai_th_1]
    
    # Kết hợp các đáp án và lời giải vào cùng một danh sách
    combined_th = list(zip(list_th_1, list_th_2))
    
    # Xáo trộn danh sách kết hợp
    random.shuffle(combined_th)
    
    # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ########################################################################
    # Vận dụng 
    ########################################################################
    
    # Các đáp án
    vd_da_1_d = '$AG_1 = G_1G_2$'
    vd_da_1_s = '\\True $AG_1 = %s G_1G_2$' % (he_so_sai_c)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vd_1 = [vd_da_1]
    
    # Nội dung lời giải
    loigiai_vd_1 = ('''Trong $(AA'C'C)$, gọi $I = A'C \\cap AC'$. \\\\ Ta có $G_1$ là trọng tâm của tam giác $A'AC$ nên $AG_1 = \\frac{2}{3}AI = \\frac{2}{3} \\cdot \\frac{1}{2}AC' = \\frac{1}{3}AC'$. \\\\ Ta có $G_2$ là trọng tâm của tam giác $A'CC'$ nên $C'G_2 = \\frac{2}{3}C'I = \\frac{2}{3} \\cdot \\frac{1}{2}AC' = \\frac{1}{3}AC'$. \\\\ Ta có $G_1G_2 = AC' - AG_1 - C'G_2 = AC' - \\frac{1}{3}AC' - \\frac{1}{3}AC' = \\frac{1}{3}AC'$. \\\\ Từ đó ta có $AG_1 = G_1G_2 = G_2C' = \\frac{1}{3}AC'$. \\\\ Vậy $AG_1 = G_1G_2$, do đó mệnh đề \"$AG_1 = %s G_1G_2$\" là sai.''' % (he_so_sai_c))
    
    # Đưa các lời giải vào danh sách lời giải
    list_vd_2 = [loigiai_vd_1]
    
    # Kết hợp các đáp án và lời giải vào cùng một danh sách
    combined_vd = list(zip(list_vd_1, list_vd_2))
    
    # Xáo trộn danh sách kết hợp
    random.shuffle(combined_vd)
    
    # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ########################################################################
    # Vận dụng cao 
    ########################################################################
    
    # Các đáp án
    vdc_da_1_d = '\\True Mặt phẳng $(A\'B\'G_2)$ cắt hình hộp $ABCD.A\'B\'C\'D\'$ tạo thành một tứ giác là hình bình hành'
    vdc_da_1_s = 'Mặt phẳng $(A\'B\'G_2)$ cắt hình hộp $ABCD.A\'B\'C\'D\'$ tạo thành một tứ giác là %s' % (hinh_sai_d)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vdc_1 = [vdc_da_1]
    
    # Nội dung lời giải
    loigiai_vdc_1 = ('''Xét tam giác $B'D'C$, gọi $P = B'G_2 \\cap CD'$. Suy ra $P$ là trung điểm của $CD'$. \\\\ Trong $(A'B'G_2)$, vẽ $Px // A'B'$. \\\\ Trong $(CC'D'D)$, $Px$ cắt $CC', DD'$ lần lượt tại $M$ và $N$. \\\\ Suy ra $MN // CD$ và $MN = CD$. \\\\ Ta có: $\\begin{cases} (A'B'G_2) \\cap (A'B'C'D') = A'B' \\\\ (A'B'G_2) \\cap (B'C'CB) = B'M \\\\ (A'B'G_2) \\cap (CC'D'D) = MN \\\\ (A'B'G_2) \\cap (AA'D'D) = NA' \\end{cases}$ \\\\ $\\Rightarrow$ Thiết diện của $(A'B'G_2)$ và hình hộp $ABCD.A'B'C'D'$ là tứ giác $A'B'MN$. \\\\ Ta có: $\\begin{cases} MN // A'B' \\\\ MN = A'B' (= CD) \\end{cases} \\Rightarrow$ Thiết diện $A'B'MN$ là hình bình hành.''')
    
    # Đưa các lời giải vào danh sách lời giải
    list_vdc_2 = [loigiai_vdc_1]
    
    # Kết hợp các đáp án và lời giải vào cùng một danh sách
    combined_vdc = list(zip(list_vdc_1, list_vdc_2))
    
    # Xáo trộn danh sách kết hợp
    random.shuffle(combined_vdc)
    
    # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
    shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)
    
    def count_true_answers(answers):
        return sum('\\True' in ans for ans in answers)
    
    # Lặp đến khi đáp án có từ 1 đến 3 đúng
    while True:
        nb_da_1 = random.choice(list_nb_da_1)
        th_da_1 = random.choice(list_th_da_1)
        vd_da_1 = random.choice(list_vd_da_1)
        vdc_da_1 = random.choice(list_vdc_da_1)
        
        answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
        true_count = count_true_answers(answers)
        
        if 1 <= true_count <= 3:
            break
    
    # Gán lại vào list
    list_nb_1 = [nb_da_1]
    list_th_1 = [th_da_1]
    list_vd_1 = [vd_da_1]
    list_vdc_1 = [vdc_da_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    combined_th = list(zip(list_th_1, list_th_2))
    combined_vd = list(zip(list_vd_1, list_vd_2))
    combined_vdc = list(zip(list_vdc_1, list_vdc_2))
    
    random.shuffle(combined_nb)
    random.shuffle(combined_th)
    random.shuffle(combined_vd)
    random.shuffle(combined_vdc)
    
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)
    
    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    content = ('\\begin{minipage}{\\textwidth} \n'
    '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
    '\\choiceTFn \n'
    '{'+str(shuffled_answers_nb[0])+'}\n'
    '{'+str(shuffled_answers_th[0])+'}\n'
    '{'+str(shuffled_answers_vd[0])+'}\n'
    '{'+str(shuffled_answers_vdc[0])+'}\n'
    '\\loigiai{ \n'
    + str(tikz_fig) + '\n'
    '\\begin{enumEX}[a)]{1} \n'
    '\\item '+str(shuffled_solutions_nb[0])+'\n'
    '\\item '+str(shuffled_solutions_th[0])+'\n'
    '\\item '+str(shuffled_solutions_vd[0])+'\n'
    '\\item '+str(shuffled_solutions_vdc[0])+'\n'
    '\\end{enumEX}} \n'
    '\\end{ex}\n'
    '\\end{minipage}\n\n')
    
    return content