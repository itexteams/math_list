import sys
from PyQt5.QtWidgets import QApplication, QColorDialog, QMainWindow, QSplitter, QTreeWidget, QSpacerItem, QSizePolicy, QTreeWidgetItem, QCheckBox, QFileDialog, QVBoxLayout, QTextEdit, QPushButton, QWidget, QLabel, QLineEdit, QDialog, QAction, QMessageBox, QScrollBar, QHeaderView, QMenu, QGridLayout
from sympy import *
from sympy.abc import x
import sympy as sp
from sympy import symbols,sqrt,evaluate,Subs,latex, Rational, expand, simplify, integrate
import random
import math
from sympy import Rational
from fractions import Fraction as frac
from random import randint
from PyQt5.QtGui import QTextCursor
from PyQt5.QtGui import QFont
import hashlib
import uuid
import os
from sympy import symbols, Eq, solve
import numpy as np
from PyQt5.QtGui import QIcon
from math import factorial
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextDocument
from subprocess import run, CalledProcessError
import shutil
from PyQt5.QtWidgets import QProgressBar
from docx import Document
from PyQt5 import QtGui
import re
import pandas as pd
from PyQt5.QtGui import QPixmap
import subprocess
import platform
import json
from decimal import Decimal, ROUND_HALF_UP
from PyQt5.QtWidgets import QComboBox, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QSpinBox, QTreeWidget, QTreeWidgetItem, QCheckBox, QTextEdit, QPushButton, QHBoxLayout
from random import randint, choice, shuffle
from sympy import latex
from fractions import Fraction
from collections import Counter
from random import sample
import shutil
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
import qrcode
import json
import glob
import os
import platform
import subprocess
import hashlib
import base64
from datetime import datetime, timedelta
from PyQt5.QtWidgets import (QApplication, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox)
from sympy import symbols, solve, Lt
#from PyQt5.QtWebEngineWidgets import QWebEngineView
#from PyQt5.QtCore import QUrl
#from sympy import latex
import re
import pyperclip
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

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


def bt_dang17_p2_b2_c1_ds12(self):
            # Khai báo biến
            def fmt_latex(val):
                if val == int(val):
                    return str(int(val))
                return latex(val)

            # Random các biến
            a = random.randint(2, 5) # Cạnh hình vuông
            val_SM = random.randint(a + 1, a + 3) # Độ dài đoạn SM

            # Tính toán cho mệnh đề c
            SA_val = a
            goc_d = 45 # Nếu SA = a thì góc 45 độ

            # Tính toán cho mệnh đề d
            # V_SAMC max khi AM = sqrt(SM^2 / 2). Sử dụng Rational để giữ nguyên căn thức đẹp trong LaTeX
            AM_max_val = sp.sqrt(Rational(val_SM**2, 2))
            AM_max_latex = latex(AM_max_val)

            # Vẽ hình TikZ
            tikz = ('''\\begin{center}
            \\begin{tikzpicture}[scale=1, line join=round, line cap=round, >=latex, line width=1pt]
            \\coordinate (A) at (0,0);
            \\coordinate (D) at (4,0);
            \\coordinate (B) at (-1,-2);
            \\coordinate (C) at ($(D)+(B)-(A)$);
            \\coordinate (S) at (0,4);
            \\coordinate (I) at ($(S)!0.5!(B)$);
            \\coordinate (K) at ($(S)!0.5!(C)$);
            \\coordinate (M) at ($(A)!0.3!(B)$);
            \\draw[dashed] (S)--(A)--(B) (A)--(D)  (A)--(C) (B)--(D) (S)--(M) (M)--(C);
            \\draw (S)--(B)--(C)--(D)--(S)--(C) (I)--(K);
            \\fill (S) circle (1.5pt) node[above] {$S$};
            \\fill (A) circle (1.5pt) node[left] {$A$};
            \\fill (B) circle (1.5pt) node[left] {$B$};
            \\fill (C) circle (1.5pt) node[right] {$C$};
            \\fill (D) circle (1.5pt) node[right] {$D$};
            \\fill (I) circle (1.5pt) node[left] {$I$};
            \\fill (K) circle (1.5pt) node[right] {$K$};
            \\fill (M) circle (1.5pt) node[below] {$M$};
            \\end{tikzpicture}
            \\end{center}''')

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình vuông cạnh bằng $%s$. Cạnh bên $SA$ vuông góc với mặt phẳng đáy. %s''' % (a, tikz))

            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Gọi $I$ và $K$ lần lượt là trung điểm của hai cạnh bên $SB$ và $SC$ thì $IK // (SAD)$'
            nb_da_1_s = 'Gọi $I$ và $K$ lần lượt là trung điểm của hai cạnh bên $SB$ và $SC$ thì $IK // (SAB)$'
            list_nb_da_1=[nb_da_1_d,nb_da_1_s]
            nb_da_1=random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Xét mệnh đề a) \\\\ Ta có $I$ là trung điểm của $SB$ và $K$ là trung điểm của $SC$ nên $IK$ là đường trung bình của $\\Delta SBC \\Rightarrow IK // BC$. \\\\ Mặt khác $ABCD$ là hình vuông nên $BC // AD \\Rightarrow IK // AD$ mà $AD \\subset (SAD) \\Rightarrow IK // (SAD)$. \\\\ Vậy mệnh đề a) đúng.''')

            # Đưa các lời giải vào danh sách lời giải
            list_nb_2 = [loigiai_nb_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_nb = list(zip(list_nb_1, list_nb_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_nb)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ######################################################################## Thông hiểu ############################################
            # Các đáp án
            th_da_1_d = '\\True Đường chéo $BD$ của mặt đáy vuông góc với mặt phẳng $(SAC)$'
            th_da_1_s = 'Đường chéo $BD$ của mặt đáy vuông góc với mặt phẳng $(SAB)$'
            list_th_da_1=[th_da_1_d,th_da_1_s]
            th_da_1=random.choice(list_th_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''Xét mệnh đề b) \\\\ Do $ABCD$ là hình vuông nên $BD \\perp AC$ mà $\\begin{cases} SA \\perp (ABCD) \\\\ BD \\subset (ABCD) \\end{cases} \\Rightarrow SA \\perp BD$. \\\\ Mặt khác $\\begin{cases} BD \\perp AC \\\\ BD \\perp SA \\end{cases} \\Rightarrow BD \\perp (SAC)$. \\\\ Vậy mệnh đề b) đúng.''')

            # Đưa các lời giải vào danh sách lời giải
            list_th_2 = [loigiai_th_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_th = list(zip(list_th_1, list_th_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_th)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## Vận dụng ############################################
            # Các đáp án
            vd_da_1_d = 'Khi $SA = AB$ thì góc nhị diện giữa mặt phẳng $(SCD)$ và mặt phẳng đáy bằng $60^\\circ$'
            vd_da_1_s = '\\True Khi $SA = AB$ thì góc nhị diện giữa mặt phẳng $(SCD)$ và mặt phẳng đáy bằng $45^\\circ$'
            list_vd_da_1=[vd_da_1_d,vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Xét mệnh đề c) \\\\ Góc nhị diện giữa $(SCD)$ và $(ABCD)$ là góc giữa hai đường thẳng lần lượt nằm trong hai mặt phẳng và cùng vuông góc với giao tuyến $CD$. \\\\ Trong mặt phẳng $(ABCD)$, ta có $AD \\perp CD$ (vì $ABCD$ là hình vuông). \\\\ Ta có: $CD \\perp AD$ và $CD \\perp SA$ (vì $SA \\perp (ABCD)$) nên suy ra $CD \\perp (SAD)$. \\\\ Vì $CD \\perp (SAD)$ nên $CD \\perp SD$. \\\\ Vậy góc giữa hai mặt phẳng $(SCD)$ và $(ABCD)$ chính là góc $\\widehat{SDA}$. \\\\ Khi $SA = x = %s$ ta có $SA = %s$. Xét tam giác vuông $SAD$, có $SA = %s$ và $AD = %s$. \\\\ Tam giác $SAD$ vuông cân tại $A$ suy ra $\\widehat{SDA} = %s^\\circ$. \\\\ Mệnh đề c) sai.''' % (a, a, a, a, goc_d))

            # Đưa các lời giải vào danh sách lời giải
            list_vd_2 = [loigiai_vd_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vd = list(zip(list_vd_1, list_vd_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vd)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## Vận dụng cao ############################################
            # Các đáp án
            vdc_da_1_d = 'Gọi $M$ là một điểm di động trên cạnh $AB$. Biết rằng độ dài đoạn thẳng $SM$ luôn bằng $%s$. Khi đó, thể tích của khối chóp $S.AMC$ đạt giá trị lớn nhất khi độ dài đoạn $AM$ bằng $%s$' % (val_SM, a)
            vdc_da_1_s = '\\True Gọi $M$ là một điểm di động trên cạnh $AB$. Biết rằng độ dài đoạn thẳng $SM$ luôn bằng $%s$. Khi đó, thể tích của khối chóp $S.AMC$ đạt giá trị lớn nhất khi độ dài đoạn $AM$ bằng $%s$' % (val_SM, AM_max_latex)
            list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Xét mệnh đề d) \\\\ Đặt $AM = y$ thì $0 < y < %s$ và $\\Delta SAM$ vuông nên $SM^2 = SA^2 + AM^2 \\Rightarrow SA = \\sqrt{%s^2 - y^2} = \\sqrt{%s - y^2}$. \\\\ Thể tích khối chóp $V_{S.AMC} = \\frac{1}{3} \\cdot SA \\cdot S_{\\Delta AMC} = \\frac{1}{3} \\cdot SA \\cdot (S_{\\Delta ABC} - S_{\\Delta MBC})$. \\\\ Ta có: $S_{\\Delta ABC} - S_{\\Delta MBC} = \\frac{1}{2} AB \\cdot BC - \\frac{1}{2} MB \\cdot BC = \\frac{1}{2} \\cdot %s \\cdot %s - \\frac{1}{2} (%s - y) \\cdot %s = \\frac{%s}{2} y \\Rightarrow V_{S.AMC} = \\frac{1}{3} \\cdot x \\cdot \\frac{%s}{2} y = \\frac{%s}{6} \\sqrt{%s - y^2} \\cdot y = f(y)$. \\\\ Khảo sát hàm số $f(y)$ trên $(0; %s)$ đạt max tại $y = %s$. \\\\ Mệnh đề d) sai.''' % (a, val_SM, val_SM**2, a, a, a, a, a, a, a, val_SM**2, a, AM_max_latex))

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
                '\\begin{ex}\n'+
                str(noidungcauhoi)+ 
                '\n\\choiceTFn \n'
                '{'+str(shuffled_answers_nb[0])+'}\n'
                '{'+str(shuffled_answers_th[0])+'}\n'
                '{'+str(shuffled_answers_vd[0])+'}\n'
                '{'+str(shuffled_answers_vdc[0])+'}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(shuffled_solutions_nb[0])+'\n'
                '\\item '+str(shuffled_solutions_th[0])+'\n'
                '\\item '+str(shuffled_solutions_vd[0])+'\n'
                '\\item '+str(shuffled_solutions_vdc[0])+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content

