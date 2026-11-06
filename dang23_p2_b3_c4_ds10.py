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


def bt_dang23_p2_b3_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến sympy
            x = symbols('x')

            # --- KHỞI TẠO DỮ LIỆU NGẪU NHIÊN ---
            # Giữ nguyên giá trị như đề bài hoặc random nhẹ để số vẫn đẹp
            h = 4 # Chiều cao cổng
            L = 8 # Chiều ngang cổng
            xA = -L/2
            xB = L/2

            # Phương trình y = ax^2 + h. Đi qua (xB, 0) => 0 = a*(xB^2) + h => a = -h/(xB^2)
            a_val = Rational(-h, int(xB**2))
            pt_p = a_val * x**2 + h

            # Các thông số cho câu d
            y_low = Rational(7, 4) # 1.75m
            y_high = 3             # 3m
            # CD = 2 * sqrt((y-h)/a)
            cd_low = 2 * sp.sqrt((y_high - h)/a_val)
            cd_high = 2 * sp.sqrt((y_low - h)/a_val)

            # Nội dung câu hỏi
            noidungcauhoi = (r'''Một chiếc cổng hình parabol có chiều cao $%sm$ và chiều ngang $%sm$. Người ta muốn thiết kế một cánh cổng bằng kính hình chữ nhật đặt ngay giữa cổng parabol đồng thời làm hai cánh cửa phụ hai bên (tham khảo hình vẽ). Gắn hệ trục tọa độ $Oxy$ sao cho chân cổng trùng với trục hoành và parabol nhận trục tung làm trục đối xứng.''' 
                             %(h, L))

            # --- TÍNH TOÁN CÁC ĐÁP ÁN ---

            ########################################################################
            # Nhận biết: Tọa độ điểm B
            nb_da_1_d = r'\True Tọa độ điểm $B$ là $B(%s;0)$ ' %(int(xB))
            nb_da_1_s = r'Tọa độ điểm $B$ là $B(0;%s)$ ' %(int(xB))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)
            loigiai_nb_1 = r'''Vì chiều ngang cổng là $%sm$ và trục tung là trục đối xứng nên chân cổng $B$ có hoành độ là $xB = %s/2 = %s$. Vậy $B(%s; 0)$.''' %(L, L, int(xB), int(xB))

            ########################################################################
            # Thông hiểu: Dạng phương trình
            th_da_1_d = r'\True Parabol là đồ thị của hàm số $(P): y = ax^2 + %s$ ' %(h)
            th_da_1_s = r'Parabol là đồ thị của hàm số $(P): y = ax^2 + %s$ ' %(int(L))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)
            loigiai_th_1 = r'''Vì đỉnh của Parabol nằm trên trục tung và có chiều cao là $%sm$ nên tọa độ đỉnh là $I(0; %s)$. Do đó phương trình có dạng $y = ax^2 + %s$.''' %(h, h, h)

            ########################################################################
            # Vận dụng: Phương trình cụ thể
            pt_latex = latex(pt_p)
            sai_pt = latex(Rational(a_val, 2) * x**2 + h)
            vd_da_1_d = r'\True Phương trình của Parabol là $y = %s$ ' %(pt_latex)
            vd_da_1_s = r'Phương trình của Parabol là $y = %s$ ' %(sai_pt)
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)
            loigiai_vd_1 = r'''Thay tọa độ $B(%s; 0)$ vào phương trình $y = ax^2 + %s$, ta có: $0 = a \cdot %s^2 + %s \Rightarrow a = %s$. \\ Vậy $(P): y = %s$.''' %(int(xB), h, int(xB), h, latex(a_val), pt_latex)

            ########################################################################
            # Vận dụng cao: Kích thước cửa
            vdc_da_1_d = r'\True Nếu muốn chiều cao của phần cổng hình chữ nhật trong khoảng từ $1,75m$ đến $3m$ thì chiều ngang của cánh cổng (đoạn $CD$) thỏa mãn $%s \le CD \le %s$ ' %(int(cd_low), int(cd_high))
            vdc_da_1_s = r'Nếu muốn chiều cao của phần cổng hình chữ nhật trong khoảng từ $1,75m$ đến $3m$ thì chiều ngang của cánh cổng (đoạn $CD$) thỏa mãn $2 \le CD \le 4$ '
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)
            loigiai_vdc_1 = r'''Gọi chiều ngang cánh cổng là $CD = 2x_0$. Khi đó chiều cao cánh cổng là $y_0 = %s x_0^2 + %s$. \\
            - Với $y_0 = 3 \Rightarrow 3 = %s x_0^2 + %s \Rightarrow x_0^2 = 4 \Rightarrow x_0 = 2 \Rightarrow CD = 4$. \\
            - Với $y_0 = 1,75 \Rightarrow 1,75 = %s x_0^2 + %s \Rightarrow x_0^2 = 9 \Rightarrow x_0 = 3 \Rightarrow CD = 6$. \\
            Vậy $%s \le CD \le %s$.''' %(latex(a_val), h, latex(a_val), h, latex(a_val), h, int(cd_low), int(cd_high))

            # --- XỬ LÝ TRỘN VÀ XUẤT NỘI DUNG ---
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                ans_list = [random.choice(list_nb_da_1), random.choice(list_th_da_1), random.choice(list_vd_da_1), random.choice(list_vdc_da_1)]
                if 1 <= count_true_answers(ans_list) <= 3:
                    shuffled_answers = ans_list
                    break

            # Ánh xạ lời giải tương ứng (trong mẫu này ta lấy lời giải cố định vì nội dung câu hỏi không đổi thứ tự a,b,c,d)
            shuffled_solutions = [loigiai_nb_1, loigiai_th_1, loigiai_vd_1, loigiai_vdc_1]

            # Xuất kết quả theo định dạng minipage và ex
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\begin{center}\n'
                '\\begin{tikzpicture}[scale=0.6, font=\\footnotesize, >=stealth]\n'
                '\\draw[->] (-5,0) -- (5,0) node[below] {$x$};\n'
                '\\draw[->] (0,-1) -- (0,5) node[left] {$y$};\n'
                '\\draw[red, thick, domain=-4:4, samples=100] plot (\\x, {-0.25*\\x*\\x + 4});\n'
                '\\draw[thick] (-2,0) -- (2,0) -- (2,3) -- (-2,3) -- cycle;\n'
                '\\fill (-4,0) circle (1.5pt) node[below left] {$A$};\n'
                '\\fill (4,0) circle (1.5pt) node[below right] {$B$};\n'
                '\\fill (-2,0) circle (1.5pt) node[below] {$C$};\n'
                '\\fill (2,0) circle (1.5pt) node[below] {$D$};\n'
                '\\fill (2,3) circle (1.5pt) node[above right] {$E$};\n'
                '\\fill (-2,3) circle (1.5pt) node[above left] {$F$};\n'
                '\\node[below left] at (0,0) {$O$};\n'
                '\\end{tikzpicture}\n'
                '\\end{center}\n'
                '\\choiceTFn \n'
                '{' + str(shuffled_answers[0]) + '}\n'
                '{' + str(shuffled_answers[1]) + '}\n'
                '{' + str(shuffled_answers[2]) + '}\n'
                '{' + str(shuffled_answers[3]) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(shuffled_solutions[0]) + '\n'
                '\\item ' + str(shuffled_solutions[1]) + '\n'
                '\\item ' + str(shuffled_solutions[2]) + '\n'
                '\\item ' + str(shuffled_solutions[3]) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

