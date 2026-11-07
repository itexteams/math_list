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


def bt_dang6_p2_b3_c1_hh11(self):
        # ==================== HÌNH VẼ TIKZ ====================
        # Hình vẽ chuẩn 100% theo mẫu
        tikz_figure = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (B) at (0,0);
\\coordinate (C) at (2.2,0.8);
\\coordinate (A) at (4.5,-0.1);
\\coordinate (D) at (6.7,0.7);
\\coordinate (S) at (3.3,4.5);
\\coordinate (O) at (intersection of A--C and B--D);
\\coordinate (M) at ($(S)!0.5!(C)$);
\\coordinate (N) at ($(S)!0.5!(A)$);
\\coordinate (P) at ($(S)!0.5!(D)$);
\\coordinate (E) at (2.3,-0.8);
\\coordinate (F) at (-2.4,0.85);
\\draw[line width=1pt] (F)--(B)--(E)--(A)--(D)--(S)--(F) (S)--(B) (S)--(A) (S)--(D) (B)--(N);
\\draw[line width=1pt, dashed] (B)--(C)--(D) (S)--(C) (A)--(C) (B)--(D) (B)--(M) (M)--(N) (M)--(P) (E)--(D) (F)--(C) (B)--(O);
\\fill (S) circle (1pt) node[above] {$S$};\n\\fill (A) circle (1pt) node[below right] {$A$};
\\fill (B) circle (1pt) node[below left] {$B$};
\\fill (C) circle (1pt) node[above right] {$C$};
\\fill (D) circle (1pt) node[right] {$D$};
\\fill (O) circle (1pt) node[above] {$O$};
\\fill (M) circle (1pt) node[above left] {$M$};
\\fill (N) circle (1pt) node[right] {$N$};
\\fill (P) circle (1pt) node[above right] {$P$};
\\fill (E) circle (1pt) node[below] {$E$};
\\fill (F) circle (1pt) node[above left] {$F$};
\\end{tikzpicture}
\\end{center}''')

        # Khai báo biến
        dinh = "S"
        day = "ABCD"
        ten_hinh = "%s.%s" % (dinh, day)
        ti_so_dung = Rational(1, 4)
        ti_so_sai_list = [Rational(1, 2), Rational(1, 3), Rational(1, 6), Rational(1, 8)]
        ti_so_sai = random.choice(ti_so_sai_list)

        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho hình chóp $%s$ có đáy là hình bình hành tâm $O$. Gọi $M, N$ và $P$ lần lượt là trung điểm của $SC, SA$ và $SD$.''' % (ten_hinh))

        ########################################################################
        # Nhận biết 
        ########################################################################
        
        # Các đáp án
        nb_da_1_d = '\\True $CD // (SAB)$'
        nb_da_1_s = '$CD$ cắt mặt phẳng $(SAB)$'
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        nb_da_1 = random.choice(list_nb_da_1)
        
        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_nb_1 = [nb_da_1]
        
        # Nội dung lời giải
        loigiai_nb_1 = ('''Ta có $\\begin{cases} CD // AB \\subset (SAB) \\\\ CD \\not\\subset (SAB) \\end{cases} \\Rightarrow CD // (SAB)$.''')
        
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
        th_da_1_d = '\\True Giao tuyến của hai mặt phẳng $(SAD)$ và $(SBC)$ là đường thẳng $d$ đi qua $S$ và song song với $AD, BC$'
        th_da_1_s = 'Giao tuyến của hai mặt phẳng $(SAD)$ và $(SBC)$ là đường thẳng $d$ đi qua $S$ và song song với $AB, CD$'
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        th_da_1 = random.choice(list_th_da_1)
        
        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_th_1 = [th_da_1]
        
        # Nội dung lời giải
        loigiai_th_1 = ('''Xét hai mặt phẳng $(SAD)$ và $(SBC)$ có: \\\\ $\\begin{cases} S \\text{ chung} \\\\ AD // BC; AD \\subset (SAD); BC \\subset (SBC) \\end{cases} \\Rightarrow$ Giao tuyến của hai mặt phẳng $(SAD)$ và $(SBC)$ là đường thẳng $d$ đi qua $S$ và song song với $AD, BC$.''')
        
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
        vd_da_1_d = '\\True Giao tuyến của hai mặt phẳng $(BMN)$ và $(ABCD)$ là đường thẳng $\\Delta$ đi qua $B$ và song song với $AC$'
        vd_da_1_s = 'Giao tuyến của hai mặt phẳng $(BMN)$ và $(ABCD)$ là đường thẳng $\\Delta$ đi qua $B$ và song song với $BD$'
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        vd_da_1 = random.choice(list_vd_da_1)
        
        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_vd_1 = [vd_da_1]
        
        # Nội dung lời giải
        loigiai_vd_1 = ('''Ta có: \\\\ $\\begin{cases} B \\in (BMN) \\cap (ABCD) \\\\ MN // AC \\\\ MN \\subset (BMN), AC \\subset (ABCD) \\end{cases} \\Rightarrow \\Delta = (BMN) \\cap (ABCD)$ với $\\Delta$ là đường thẳng đi qua $B$ và song song với $MN, AC$.''')
        
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
        vdc_da_1_d = '\\True Gọi $E, F$ lần lượt là giao điểm của mặt phẳng $(BMN)$ với các đường thẳng $AD, CD$. Khi đó $\\dfrac{MN}{EF} = %s$' % (latex(ti_so_dung))
        vdc_da_1_s = 'Gọi $E, F$ lần lượt là giao điểm của mặt phẳng $(BMN)$ với các đường thẳng $AD, CD$. Khi đó $\\dfrac{MN}{EF} = %s$' % (latex(ti_so_sai))
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        vdc_da_1 = random.choice(list_vdc_da_1)
        
        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_vdc_1 = [vdc_da_1]
        
        # Nội dung lời giải
        loigiai_vdc_1 = ('''Xét giao tuyến của mặt phẳng $(BMN)$ và $(ABCD)$ có: \\\\ $\\begin{cases} B \\text{ chung} \\\\ MN // AC; MN \\subset (BMN); AC \\subset (ABCD) \\end{cases} \\Rightarrow$ Giao tuyến của hai mặt phẳng $(BMN)$ và $(ABCD)$ là đường thẳng $\\Delta$ đi qua $B$ và song song với $AC$. \\\\ Vì $E, F$ lần lượt là giao điểm của mặt phẳng $(BMN)$ với các đường thẳng $AD, CD$ nên trong mặt phẳng $(ABCD)$ ta có: $\\begin{cases} E = AD \\cap \\Delta \\\\ F = CD \\cap \\Delta \\end{cases}$ \\\\ Ta có $AC = 2MN$. \\\\ Vì $AC // EF \\Rightarrow \\dfrac{AC}{EF} = \\dfrac{DC}{DF} = \\dfrac{DO}{DB} = \\dfrac{1}{2} \\Rightarrow \\dfrac{2MN}{EF} = \\dfrac{1}{2} \\Rightarrow \\dfrac{MN}{EF} = \\dfrac{1}{4}$.''')
        
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