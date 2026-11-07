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


def bt_dang8_p2_b3_c1_hh11(self):
        # ==================== RANDOM BÀI TOÁN ====================
        # Hoán vị các đỉnh đáy của tam giác ABC để sinh ra nhiều mã đề khác nhau
        ds_hoan_vi = [
            ("A", "B", "C"),
        ]
        dinh_A, dinh_B, dinh_C = random.choice(ds_hoan_vi)
        dinh_S = "S"
        
        ten_chop = "%s.%s%s%s" % (dinh_S, dinh_A, dinh_B, dinh_C)
        canh_1 = "%s%s" % (dinh_A, dinh_B)
        canh_2 = "%s%s" % (dinh_B, dinh_C)
        canh_day = "%s%s" % (dinh_A, dinh_C)
        
        tg_1 = "%s%s%s" % (dinh_S, dinh_A, dinh_B)
        tg_2 = "%s%s%s" % (dinh_S, dinh_B, dinh_C)
        mp_SIJ = "%sIJ" % (dinh_S)
        mp_SAC = "%s%s" % (dinh_S, canh_day)
        mp_BHK = "%sHK" % (dinh_B)
        mp_ABC = "%s%s%s" % (dinh_A, dinh_B, dinh_C)
        duong_Bx = "%sx" % (dinh_B)
        
        # ==================== HÌNH VẼ TIKZ CHUẨN XÁC 100% ====================
        tikz_figure = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (C) at (0,0);
\\coordinate (B) at (3.5,-1.6);
\\coordinate (A) at (5.2,0);
\\coordinate (S) at (1.2,4.0);
\\coordinate (I) at ($(B)!0.5!(C)$);
\\coordinate (J) at ($(A)!0.5!(B)$);
\\coordinate (H) at ($(S)!0.667!(I)$);
\\coordinate (K) at ($(S)!0.667!(J)$);
\\coordinate (E) at ($(S)!0.5!(B)$);
\\draw[line width=1pt] (S)--(C) (S)--(B) (S)--(A) (C)--(B)--(A) (S)--(I) (S)--(J) (B)--(H) (B)--(K) (C)--(H)--(E) (A)--(K)--(E);
\\draw[line width=1pt, dashed] (C)--(A) (I)--(J) (H)--(K);
\\fill (S) circle (1pt) node[above] {$%s$};
\\fill (C) circle (1pt) node[left] {$%s$};
\\fill (B) circle (1pt) node[below] {$%s$};
\\fill (A) circle (1pt) node[right] {$%s$};
\\fill (I) circle (1pt) node[below left] {$I$};
\\fill (J) circle (1pt) node[below right] {$J$};
\\fill (H) circle (1pt) node[above left] {$H$};
\\fill (K) circle (1pt) node[above right] {$K$};
\\end{tikzpicture}
\\end{center}''' % (dinh_S, dinh_C, dinh_B, dinh_A))
        
        # ==================== NỘI DUNG CÂU HỎI ====================
        noidungcauhoi = ('''Cho hình chóp $%s$. Gọi $I, J$ lần lượt là trung điểm của $%s$ và $%s$. Gọi $H, K$ lần lượt là trọng tâm của $\\Delta %s$ và $\\Delta %s$. Khi đó:''' % (ten_chop, canh_1, canh_2, tg_1, tg_2))
        
        ########################################################################
        # Nhận biết (Ý a)
        ########################################################################
        
        # Các đáp án
        nb_da_1_d = '\\True $%s // (%s)$' % (canh_day, mp_SIJ)
        nb_da_1_s = '$%s$ cắt với mặt phẳng $(%s)$' % (canh_day, mp_SIJ)
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        nb_da_1 = random.choice(list_nb_da_1)
        
        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_nb_1 = [nb_da_1]
        
        # Nội dung lời giải
        loigiai_nb_1 = ('''Vì $IJ$ là đường trung bình $\\Delta %s$ nên $IJ // %s$. \\\\ Ta có: $\\begin{cases} %s // IJ \\\\ IJ \\subset (%s) \\\\ %s \\not\\subset (%s) \\end{cases} \\Rightarrow %s // (%s)$.''' % (mp_ABC, canh_day, canh_day, mp_SIJ, canh_day, mp_SIJ, canh_day, mp_SIJ))
        
        # Đưa các lời giải vào danh sách lời giải
        list_nb_2 = [loigiai_nb_1]
        
        # Kết hợp các đáp án và lời giải vào cùng một danh sách
        combined_nb = list(zip(list_nb_1, list_nb_2))
        
        # Xáo trộn danh sách kết hợp
        random.shuffle(combined_nb)
        
        # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
        shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
        
        ########################################################################
        # Thông hiểu (Ý b)
        ########################################################################
        
        # Các đáp án
        th_da_1_d = '\\True $HK // IJ$'
        th_da_1_s = '$HK$ cắt $IJ$'
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        th_da_1 = random.choice(list_th_da_1)
        
        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_th_1 = [th_da_1]
        
        # Nội dung lời giải
        loigiai_th_1 = ('''Ta có $\\dfrac{SH}{HI} = \\dfrac{SK}{KJ} = 2$ ($H, K$ lần lượt là trọng tâm $\\Delta %s$ và $\\Delta %s$). \\\\ Suy ra $HK // IJ$.''' % (tg_1, tg_2))
        
        # Đưa các lời giải vào danh sách lời giải
        list_th_2 = [loigiai_th_1]
        
        # Kết hợp các đáp án và lời giải vào cùng một danh sách
        combined_th = list(zip(list_th_1, list_th_2))
        
        # Xáo trộn danh sách kết hợp
        random.shuffle(combined_th)
        
        # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
        shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
        
        ########################################################################
        # Vận dụng (Ý c)
        ########################################################################
        
        # Các đáp án
        vd_da_1_d = '\\True $HK // (%s)$' % (mp_SAC)
        vd_da_1_s = '$HK$ cắt với mặt phẳng $(%s)$' % (mp_SAC)
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        vd_da_1 = random.choice(list_vd_da_1)
        
        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_vd_1 = [vd_da_1]
        
        # Nội dung lời giải
        loigiai_vd_1 = ('''Lại có $\\begin{cases} HK // %s \\ (HK // IJ, %s // IJ) \\\\ %s \\subset (%s) \\\\ HK \\not\\subset (%s) \\end{cases} \\Rightarrow HK // (%s)$.''' % (canh_day, canh_day, canh_day, mp_SAC, mp_SAC, mp_SAC))
        
        # Đưa các lời giải vào danh sách lời giải
        list_vd_2 = [loigiai_vd_1]
        
        # Kết hợp các đáp án và lời giải vào cùng một danh sách
        combined_vd = list(zip(list_vd_1, list_vd_2))
        
        # Xáo trộn danh sách kết hợp
        random.shuffle(combined_vd)
        
        # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
        shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
        
        ########################################################################
        # Vận dụng cao (Ý d)
        ########################################################################
        
        # Các đáp án
        vdc_da_1_d = '\\True Giao tuyến của $(%s)$ và $(%s)$ là đường thẳng đi qua $%s$ và song song với $%s$' % (mp_BHK, mp_ABC, dinh_B, canh_day)
        vdc_da_1_s = 'Giao tuyến của $(%s)$ và $(%s)$ là đường thẳng đi qua $%s$ và song song với $%s$' % (mp_BHK, mp_ABC, dinh_B, canh_1)
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        vdc_da_1 = random.choice(list_vdc_da_1)
        
        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_vdc_1 = [vdc_da_1]
        
        # Nội dung lời giải
        loigiai_vdc_1 = ('''Ta có $\\begin{cases} HK // %s \\\\ HK \\subset (%s) \\\\ %s \\subset (%s) \\\\ %s \\in (%s) \\cap (%s) \\end{cases}$. \\\\ Vậy giao tuyến của $(%s)$ và $(%s)$ là đường thẳng $%s$ đi qua $%s$ và song song với $%s$ và $HK$.''' % (canh_day, mp_BHK, canh_day, mp_ABC, dinh_B, mp_BHK, mp_ABC, mp_BHK, mp_ABC, duong_Bx, dinh_B, canh_day))
        
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
        
        # Xuất câu hỏi theo đúng mẫu
        content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
        '\\choiceTFn \n'
        '{'+str(shuffled_answers_nb[0])+'}\n'
        '{'+str(shuffled_answers_th[0])+'}\n'
        '{'+str(shuffled_answers_vd[0])+'}\n'
        '{'+str(shuffled_answers_vdc[0])+'}\n'
        '\\loigiai{ \n'
        + str(tikz_figure) + '\n'
        '\\begin{enumEX}[a)]{1} \n'
        '\\item '+str(shuffled_solutions_nb[0])+'\n'
        '\\item '+str(shuffled_solutions_th[0])+'\n'
        '\\item '+str(shuffled_solutions_vd[0])+'\n'
        '\\item '+str(shuffled_solutions_vdc[0])+'\n'
        '\\end{enumEX}} \n'
        '\\end{ex}\n'
        '\\end{minipage}\n\n')
        
        return content