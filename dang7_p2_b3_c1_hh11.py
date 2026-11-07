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


def bt_dang7_p2_b3_c1_hh11(self):
        # ==================== HÌNH VẼ TIKZ ====================
        tikz_figure = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (1.8,4.2);
\\coordinate (B) at (0.2,1.2);
\\coordinate (C) at (1.5,-0.6);
\\coordinate (D) at (5.2,1.2);
\\coordinate (M) at ($(B)!0.42!(C)$);
\\coordinate (N) at ($(B)!0.42!(D)$);
\\coordinate (P) at ($(A)!0.42!(D)$);
\\coordinate (Q) at ($(A)!0.42!(C)$);
\\draw[line width=1pt] (A)--(B)--(C)--(D)--(A)--(C) (M)--(Q)--(P);
\\draw[line width=1pt, dashed] (B)--(D) (M)--(N)--(P);
\\fill (A) circle (1pt) node[above] {$A$};
\\fill (B) circle (1pt) node[left] {$B$};
\\fill (C) circle (1pt) node[below] {$C$};
\\fill (D) circle (1pt) node[right] {$D$};
\\fill (M) circle (1pt) node[below left] {$M$};
\\fill (N) circle (1pt) node[below] {$N$};
\\fill (P) circle (1pt) node[above right] {$P$};
\\fill (Q) circle (1pt) node[left] {$Q$};
\\end{tikzpicture}
\\end{center}''')

        # Khai báo biến
        ten_tu_dien = "ABCD"
        canh_chua_M = "BC"
        canh_ss_1 = "AB"
        canh_ss_2 = "CD"

        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho tứ diện $%s$. Giả sử $M$ thuộc đoạn thẳng $%s$. Mặt phẳng $(\\alpha)$ qua $M$ song song với $%s$ và $%s$. Khi đó:''' % (ten_tu_dien, canh_chua_M, canh_ss_1, canh_ss_2))

        ########################################################################
        # Nhận biết 
        ########################################################################
        
        # Các đáp án
        nb_da_1_d = '\\True Giao tuyến của mặt phẳng $(\\alpha)$ với mặt phẳng $(ABC)$ là đường thẳng đi qua $M$ và song song với $AB$'
        nb_da_1_s = 'Giao tuyến của mặt phẳng $(\\alpha)$ với mặt phẳng $(ABC)$ là đường thẳng đi qua $M$ và song song với $AC$'
        list_nb_da_1=[nb_da_1_d,nb_da_1_s]
        nb_da_1=random.choice(list_nb_da_1)
        
        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_nb_1 = [nb_da_1]
        
        # Nội dung lời giải
        loigiai_nb_1 = ('''Vì $(\\alpha) // AB$ nên giao tuyến của mặt phẳng $(\\alpha)$ với mặt phẳng $(ABC)$ là đường thẳng đi qua $M$ và song song với $AB$ và cắt $AC$ tại $Q$.''')
        
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
        th_da_1_d = '\\True Giao tuyến của mặt phẳng $(\\alpha)$ với mặt phẳng $(BCD)$ là đường thẳng đi qua $M$ và song song với $CD$'
        th_da_1_s = 'Giao tuyến của mặt phẳng $(\\alpha)$ với mặt phẳng $(BCD)$ là đường thẳng đi qua $M$ và song song với $BD$'
        list_th_da_1=[th_da_1_d,th_da_1_s]
        th_da_1=random.choice(list_th_da_1)
        
        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_th_1 = [th_da_1]
        
        # Nội dung lời giải
        loigiai_th_1 = ('''Vì $(\\alpha) // CD$ nên giao tuyến của mặt phẳng $(\\alpha)$ với mặt phẳng $(BCD)$ là đường thẳng đi qua $M$ và song song với $CD$ và cắt $BD$ tại $N$.''')
        
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
        vd_da_1_d = '\\True Giao tuyến của mặt phẳng $(\\alpha)$ với mặt phẳng $(ABD)$ là đường thẳng đi qua $N$ và song song với $AB$'
        vd_da_1_s = 'Giao tuyến của mặt phẳng $(\\alpha)$ với mặt phẳng $(ABD)$ là đường thẳng đi qua $N$ và song song với $AD$'
        list_vd_da_1=[vd_da_1_d,vd_da_1_s]
        vd_da_1=random.choice(list_vd_da_1)
        
        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_vd_1 = [vd_da_1]
        
        # Nội dung lời giải
        loigiai_vd_1 = ('''Vì $(\\alpha) // AB$ nên giao tuyến của mặt phẳng $(\\alpha)$ với mặt phẳng $(ABD)$ là đường thẳng đi qua $N$ và song song với $AB$ và cắt $AD$ tại $P$.''')
        
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
        vdc_da_1_d = '\\True Hình tạo bởi các giao tuyến của mặt phẳng $(\\alpha)$ với các mặt của tứ diện (ta gọi là thiết diện) là hình bình hành'
        vdc_da_1_s = 'Hình tạo bởi các giao tuyến của mặt phẳng $(\\alpha)$ với các mặt của tứ diện (ta gọi là thiết diện) là hình thang'
        list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
        vdc_da_1=random.choice(list_vdc_da_1)
        
        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_vdc_1 = [vdc_da_1]
        
        # Nội dung lời giải
        loigiai_vdc_1 = ('''Ta có $MN // PQ // CD$ và $MQ // PN // AB$. \\\\ Vậy hình tạo bởi các giao tuyến của mặt phẳng $(\\alpha)$ với các mặt của tứ diện (ta gọi là thiết diện) là hình bình hành $MNPQ$.''')
        
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