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


def bt_dang8_p2_b4_c1_hh11(self):
        # ==================== HÌNH VẼ TIKZ ====================
        # Hình vẽ TikZ chuẩn 100% theo mẫu ảnh
        tikz_fig = ('''\\begin{center}
\\begin{tikzpicture}[scale=0.8, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (B) at (0,0);
    \\coordinate (C) at (4.5,-0.6);
    \\coordinate (A) at (2.2,1.8);
    \\coordinate (D) at ($(C)+(A)-(B)$);
    \\coordinate (E) at (1.5,4.6);
    \\coordinate (F) at ($(A)+(E)-(B)$);
    \\coordinate (S) at ($(A)!0.5!(B)$);
    \\coordinate (M) at ($(E)!0.66667!(S)$);
    \\coordinate (I) at ($(B)!0.33333!(A)$);
    \\coordinate (N) at ($(C)!0.33333!(A)$);
    \\coordinate (J) at ($(E)!0.33333!(F)$);
    \\coordinate (K) at ($(C)!0.33333!(D)$);
    \\draw[line width=1pt] (B)--(C)--(D)--(F)--(E)--(B) (E)--(C) (J)--(K);
    \\draw[line width=1pt, dashed] (B)--(A)--(D) (A)--(F) (A)--(C) (E)--(A) (E)--(S) (I)--(M) (I)--(S) (I)--(N) (J)--(E) (N)--(C);
    \\fill (B) circle (1pt) node[below left] {$B$};
    \\fill (C) circle (1pt) node[below] {$C$};
    \\fill (D) circle (1pt) node[right] {$D$};
    \\fill (A) circle (1pt) node[above right] {$A$};
    \\fill (E) circle (1pt) node[above left] {$E$};
    \\fill (F) circle (1pt) node[above] {$F$};
    \\fill (S) circle (1pt) node[below] {$S$};
    \\fill (M) circle (1pt) node[left] {$M$};
    \\fill (I) circle (1pt) node[below left] {$I$};
    \\fill (N) circle (1pt) node[below] {$N$};
    \\fill (J) circle (1pt) node[above] {$J$};
    \\fill (K) circle (1pt) node[below right] {$K$};
\\end{tikzpicture}
\\end{center}''')
        
        # Khai báo biến và tạo ngẫu nhiên tỉ số sai
        wrong_ratio = random.choice([3, 4, "\\frac{1}{2}", "\\frac{3}{2}"])
        
        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho hình bình hành $ABCD$ và $ABEF$ nằm ở hai mặt phẳng khác nhau. Gọi $M$ là trọng tâm $\\Delta ABE$. Gọi $(P)$ là mặt phẳng đi qua $M$ và song song với mặt $(ADF)$. Lấy $N$ là giao điểm của $(P)$ và $AC$.''')
        
        ########################################################################
        # Nhận biết 
        ########################################################################
        
        # Các đáp án
        nb_da_1_d = '$EFDC$ là hình bình hành'
        nb_da_1_s = '\\True $EFDC$ là hình thang'
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        nb_da_1 = random.choice(list_nb_da_1)
        
        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_nb_1 = [nb_da_1]
        
        # Nội dung lời giải
        loigiai_nb_1 = ('''Ta có: $\\begin{cases} EF // CD (// AB) \\\\ EF = CD (= AB) \\end{cases} \\Rightarrow EFDC$ là hình bình hành. \\\\ Do đó mệnh đề \"$EFDC$ là hình thang\" là sai.''')
        
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
        th_da_1_d = '\\True $FD // EC$'
        th_da_1_s = '$FD$ cắt $EC$'
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        th_da_1 = random.choice(list_th_da_1)
        
        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_th_1 = [th_da_1]
        
        # Nội dung lời giải
        loigiai_th_1 = ('''Vì $EFDC$ là hình bình hành nên suy ra $FD // EC$.''')
        
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
        vd_da_1_d = '\\True $(ADF) // (BCE)$'
        vd_da_1_s = '$(ADF)$ cắt $(BCE)$'
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        vd_da_1 = random.choice(list_vd_da_1)
        
        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_vd_1 = [vd_da_1]
        
        # Nội dung lời giải
        loigiai_vd_1 = ('''Ta có: $\\begin{cases} AD // BC; AF // BE \\\\ AD, AF \\subset (ADF); AD \\cap AF = A \\\\ BC, BE \\subset (BCE); BC \\cap BE = B \\end{cases} \\Rightarrow (ADF) // (BCE)$.''')
        
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
        vdc_da_1_d = '$\\frac{AN}{NC} = 2$'
        vdc_da_1_s = '\\True $\\frac{AN}{NC} = %s$' % (wrong_ratio)
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        vdc_da_1 = random.choice(list_vdc_da_1)
        
        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_vdc_1 = [vdc_da_1]
        
        # Nội dung lời giải
        loigiai_vdc_1 = ('''Vẽ mặt phẳng $(P)$ chứa $M$ và $(P) // (ADF)$ cắt $AB, AC, CD, EF$ lần lượt tại $I, N, K, J$. \\\\ Gọi $S$ là trung điểm của $AB$. \\\\ Ta có: $\\frac{AI}{BI} = \\frac{AN}{NC}$ (do $IN // BC$). \\\\ Ta có: $\\frac{EJ}{IS} = \\frac{ME}{MS} = 2$ (do $IS // JE$). \\\\ $BI = EJ$ (tứ giác $BIJE$ là hình bình hành) $\\Rightarrow \\frac{BI}{IS} = 2 \\Rightarrow \\frac{BI}{2} = \\frac{IS}{1} = \\frac{BI+IS}{2+1} = \\frac{BS}{3} \\Rightarrow BI = \\frac{2}{3}BS; IS = \\frac{1}{3}BS$. \\\\ Ta có: $AI = AS + IS = BS + \\frac{1}{3}BS = \\frac{4}{3}BS \\Rightarrow \\frac{AI}{BI} = \\frac{\\frac{4}{3}BS}{\\frac{2}{3}BS} = 2 \\Rightarrow \\frac{AN}{NC} = 2$. \\\\ Do đó mệnh đề \"$\\frac{AN}{NC} = %s$\" là sai.''' % (wrong_ratio))
        
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