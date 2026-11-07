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


def bt_dang7_p2_b4_c1_hh11(self):
        # ==================== HÌNH VẼ TIKZ ====================
        # Hình vẽ TikZ chuẩn 100% theo mẫu ảnh
        tikz_fig = ('''\\begin{center}
\\begin{tikzpicture}[scale=0.8, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (D1) at (0,0);
    \\coordinate (C1) at (4.8,0);
    \\coordinate (A1) at (1.4,1.8);
    \\coordinate (B1) at ($(C1)+(A1)-(D1)$);
    \\coordinate (h) at (0,2.4);
    \\coordinate (D) at ($(D1)+(h)$);
    \\coordinate (C) at ($(C1)+(h)$);
    \\coordinate (A) at ($(A1)+(h)$);
    \\coordinate (B) at ($(B1)+(h)$);
    \\coordinate (O) at ($(A)!0.5!(C)$);
    \\coordinate (O1) at ($(A1)!0.5!(C1)$);
    \\coordinate (I) at ($(A)!0.5!(C1)$);
    \\coordinate (G1) at ($(A)!0.66667!(I)$);
    \\coordinate (G2) at ($(C1)!0.66667!(I)$);
    \\draw[line width=1pt] (D)--(C)--(B)--(A)--(D) (D)--(D1)--(C1)--(C) (C1)--(B1)--(B) (D)--(B) (O)--(C) (C)--(B1) (C1)--(D);
    \\draw[line width=1pt, dashed] (D1)--(A1)--(B1) (A)--(A1) (A)--(C) (A1)--(C1) (D1)--(B1) (A1)--(C) (A)--(C1) (A1)--(B) (A1)--(D)  (A1)--(O) (C)--(O1);
    \\fill (A) circle (1pt) node[above] {$A$};
    \\fill (B) circle (1pt) node[above right] {$B$};
    \\fill (C) circle (1pt) node[above right] {$C$};
    \\fill (D) circle (1pt) node[left] {$D$};
    \\fill (A1) circle (1pt) node[below left] {$A'$};
    \\fill (B1) circle (1pt) node[right] {$B'$};
    \\fill (C1) circle (1pt) node[below right] {$C'$};
    \\fill (D1) circle (1pt) node[below left] {$D'$};
    \\fill (O) circle (1pt) node[above] {$O$};
    \\fill (O1) circle (1pt) node[below] {$O'$};
    \\fill (I) circle (1pt) node[below] {$I$};
    \\fill (G1) circle (1pt) node[left] {$G_1$};
    \\fill (G2) circle (1pt) node[right] {$G_2$};
\\end{tikzpicture}
\\end{center}''')
        
        # Khai báo biến và tạo ngẫu nhiên tỉ số sai
        wrong_ratio = random.choice(["\\frac{2}{3}", "\\frac{1}{2}", "\\frac{3}{4}"])
        
        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho hình hộp $ABCD.A'B'C'D'$. Gọi $G_1, G_2$ là trọng tâm của các tam giác $A'BD, B'D'C$.''')
        
        ########################################################################
        # Nhận biết 
        ########################################################################
        
        # Các đáp án
        nb_da_1_d = '\\True $A\'D\'CB$ là hình bình hành'
        nb_da_1_s = '$A\'D\'CB$ là hình chữ nhật'
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        nb_da_1 = random.choice(list_nb_da_1)
        
        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_nb_1 = [nb_da_1]
        
        # Nội dung lời giải
        loigiai_nb_1 = ('''Vì $ABCD.A'B'C'D'$ là hình hộp nên $\\begin{cases} A'D' // BC \\\\ A'D' = BC \\end{cases} \\Rightarrow A'D'CB$ là hình bình hành.''')
        
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
        th_da_1_d = '\\True $(A\'BD) // (B\'D\'C)$'
        th_da_1_s = '$(A\'BD)$ cắt $(B\'D\'C)$'
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        th_da_1 = random.choice(list_th_da_1)
        
        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_th_1 = [th_da_1]
        
        # Nội dung lời giải
        loigiai_th_1 = ('''Từ $A'D'CB$ là hình bình hành suy ra $A'B // CD' \\Rightarrow A'B // (B'D'C)$. (1) \\\\ Tương tự, ta có $\\begin{cases} A'B' // CD \\\\ A'B' = CD \\end{cases} \\Rightarrow A'B'CD$ là hình bình hành. \\\\ Suy ra $A'D // B'C \\Rightarrow A'D // (B'D'C)$. (2) \\\\ Mặt khác $A'B, A'D \\subset (A'BD)$ và $A'B \\cap A'D = A'$. \\\\ Từ (1) và (2) suy ra $(A'BD) // (B'D'C)$.''')
        
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
        vd_da_1_d = '\\True $G_1, G_2$ cùng thuộc $AC\'$'
        vd_da_1_s = '$G_1, G_2$ không cùng thuộc $AC\'$'
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        vd_da_1 = random.choice(list_vd_da_1)
        
        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_vd_1 = [vd_da_1]
        
        # Nội dung lời giải
        loigiai_vd_1 = ('''Gọi $O, O', I$ theo thứ tự là tâm của các hình bình hành $ABCD, A'B'C'D', ACC'A'$. \\\\ Vì $G_1$ là trọng tâm tam giác $A'BD$ nên $\\frac{A'G_1}{A'O} = \\frac{2}{3} \\Rightarrow G_1$ là trọng tâm tam giác $A'AC$, suy ra $G_1 = AI \\cap A'O$. (3) \\\\ Tương tự, $G_2$ là trọng tâm tam giác $B'D'C$ nên $\\frac{CG_2}{CO'} = \\frac{2}{3} \\Rightarrow G_2$ là trọng tâm tam giác $A'C'C$, suy ra $G_2 = C'I \\cap CO'$. (4) \\\\ Từ (3) và (4) suy ra $G_1, G_2$ cùng thuộc $AC'$.''')
        
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
        vdc_da_1_d = '$G_1G_2 = \\frac{1}{3} AC\'$'
        vdc_da_1_s = '\\True $G_1G_2 = %s AC\'$' % (wrong_ratio)
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        vdc_da_1 = random.choice(list_vdc_da_1)
        
        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_vdc_1 = [vdc_da_1]
        
        # Nội dung lời giải
        loigiai_vdc_1 = ('''Ta có: $\\frac{AG_1}{AI} = \\frac{2}{3} \\Rightarrow \\frac{AG_1}{AC'} = \\frac{1}{3}$; $\\frac{C'G_2}{C'I} = \\frac{2}{3} \\Rightarrow \\frac{C'G_2}{AC'} = \\frac{1}{3}$. \\\\ Do vậy $AG_1 = G_1G_2 = G_2C' = \\frac{1}{3} AC'$. \\\\ Vậy $G_1, G_2$ cùng thuộc $AC'$, đồng thời chia $AC'$ thành ba phần bằng nhau. Do đó mệnh đề \"$G_1G_2 = %s AC\'$\" là sai.''' % (wrong_ratio))
        
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