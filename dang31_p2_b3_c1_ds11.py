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


def bt_dang31_p2_b3_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # --- NGẪU NHIÊN HÓA CÁC THAM SỐ BÀI TOÁN ---
            # Khởi tạo tham số ngẫu nhiên cho câu a, b, d
            he_so_a = random.choice([2, 3, 4])  # Hệ số góc cho câu a

            # Tham số cho câu b: tan(2x - phi)
            phi_list = [Rational(1, 6), Rational(1, 4), Rational(1, 3)]
            phi = random.choice(phi_list)  # Chọn ngẫu nhiên góc pha ban đầu (pi/6, pi/4, pi/3)
            # Tính tập xác định đúng cho tan(2x - phi): 2x - phi != pi/2 + k*pi <=> 2x != pi/2 + phi + k*pi
            tu_so_b = Rational(1, 2) + phi
            mau_so_b = 2
            tu_so_b_rutgon = tu_so_b / mau_so_b  # (1/2 + phi)/2 = 1/4 + phi/2

            # Tham số cho câu e (trong code đóng vai trò là phần d): y = sin^2(x) - cos(x) + m
            m_val = random.choice([1, 2, 3])  # Hệ số tự do của hàm bậc hai
            max_val_frac = Rational(5, 4) + m_val
            max_val_sai_frac = Rational(3, 4) + m_val

            # Biểu diễn các chuỗi hiển thị
            str_phi = latex(phi) + '\\pi' if phi != 1 else '\\pi'
            str_phi_xong = "\\tan\\left( 2x - \\frac{\\pi}{%s} \\right)" % (latex(phi.denominator))

            str_txd_b_tu = (1 * phi.denominator + 2 * phi.numerator)
            str_txd_b_mau = (4 * phi.denominator)
            str_txd_b_frac = "\\frac{%s\\pi}{%s}" % (latex(str_txd_b_tu), latex(str_txd_b_mau))

            # Nội dung câu hỏi
            noidungcauhoi = ('''Xét tính đúng - sai của các phát biểu sau:''')

            ########################################################################
            # Nhận biết ############################################
            nb_da_1_d = '\\True Tập xác định của hàm số $y = \\sin %sx$ là $\\mathbb{R}$' % (latex(he_so_a))
            nb_da_1_s = 'Tập xác định của hàm số $y = \\sin %sx$ là $\\mathbb{R} \\setminus \\{0\\}$' % (latex(he_so_a))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            list_nb_1 = [nb_da_1]

            loigiai_nb_1 = ('''Hàm số lượng giác $y = \\sin u(x)$ luôn xác định với mọi giá trị của $u(x)$.\\\\
            Vì biểu thức $u(x) = %sx$ là đa thức xác định trên toàn bộ trục số, nên tập xác định của hàm số $y = \\sin %sx$ là $\\mathbb{R}$.''' 
                            % (latex(he_so_a), latex(he_so_a)))

            list_nb_2 = [loigiai_nb_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu ############################################
            th_da_1_d = '\\True Tập xác định của hàm số $y = %s$ là: $\\mathbb{R} \\setminus \\left\\{ %s + k\\frac{\\pi}{2} \\right\\}$, $k \\in \\mathbb{Z}$' % (str_phi_xong, str_txd_b_frac)
            th_da_1_s = 'Tập xác định của hàm số $y = %s$ là: $\\mathbb{R} \\setminus \\left\\{ \\frac{\\pi}{%s} + k\\pi \\right\\}$, $k \\in \\mathbb{Z}$' % (str_phi_xong, latex(phi.denominator))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            list_th_1 = [th_da_1]

            loigiai_th_1 = ('''Hàm số $y = %s$ xác định khi và chỉ khi:\\\\
            $2x - \\frac{\\pi}{%s} \\neq \\frac{\\pi}{2} + k\\pi \\Leftrightarrow 2x \\neq \\frac{\\pi}{2} + \\frac{\\pi}{%s} + k\\pi$\\\\
            $\\Leftrightarrow 2x \\neq \\frac{%s\\pi}{%s} + k\\pi \\Leftrightarrow x \\neq %s + k\\frac{\\pi}{2}$ ($k \\in \\mathbb{Z}$).\\\\
            Vậy tập xác định của hàm số là: $\\mathbb{R} \\setminus \\left\\{ %s + k\\frac{\\pi}{2} \\right\\}$, $k \\in \\mathbb{Z}$.''' 
                            % (str_phi_xong, latex(phi.denominator), latex(phi.denominator), latex(1 * phi.denominator + 2 * phi.numerator), latex(2 * phi.denominator), str_txd_b_frac, str_txd_b_frac))

            list_th_2 = [loigiai_th_1]

            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ########################################################################
            # Vận dụng ############################################
            vd_da_1_d = '\\True Đường cong trong hình dưới đây là đồ thị của hàm số $y = -\\sin x$'
            vd_da_1_s = 'Đường cong trong hình dưới đây là đồ thị của hàm số $y = \\sin x$'
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            list_vd_1 = [vd_da_1]

            loigiai_vd_1 = ('''Dựa vào hình ảnh minh họa đồ thị đường cong:\\\\
            \\begin{center}
            \\begin{tikzpicture}[scale=1.0, line width=1pt, >=stealth]
                \\draw[->, color=blue] (-5.5,0) -- (5.5,0) node[right, color=black] {$x$};
                \\draw[->, color=blue] (0,-2.2) -- (0,2.2) node[above, color=black] {$y$};
                \\draw[dashed, color=blue!50] (-4.71,1) -- (0,1) node[above right, color=black] {1};
                \\draw[dashed, color=blue!50] (1.57,-1) -- (0,-1) node[below left, color=black] {-1};
                \\draw[dashed, color=blue!50] (-1.57,1) -- (-1.57,0);
                \\draw[dashed, color=blue!50] (1.57,-1) -- (1.57,0);
                \\draw[dashed, color=blue!50] (4.71,1) -- (4.71,0);
                \\draw[dashed, color=blue!50] (-4.71,-1) -- (-4.71,0);
                \\draw[smooth, samples=100, domain=-5.2:5.2, color=brown] plot (\\x, {-sin(\\x r)});
                \\filldraw (0,0) circle (1.5pt) node[below left] {O};
                \\filldraw (3.14,0) circle (1.5pt) node[below right] {$\\pi$};
                \\filldraw (-3.14,0) circle (1.5pt) node[below left] {$-\\pi$};
                \\filldraw (1.57,0) circle (1.5pt) node[below] {$\\frac{\\pi}{2}$};
                \\filldraw (-1.57,0) circle (1.5pt) node[below] {$-\\frac{\\pi}{2}$};
                \\filldraw (4.71,0) circle (1.5pt) node[above] {$\\frac{3\\pi}{2}$};
                \\filldraw (-4.71,0) circle (1.5pt) node[below] {$-\\frac{3\\pi}{2}$};
                \\filldraw (1.57,-1) circle (1.5pt);
                \\filldraw (-1.57,1) circle (1.5pt);
                \\filldraw (4.71,1) circle (1.5pt);
                \\filldraw (-4.71,-1) circle (1.5pt);
            \\end{tikzpicture}
            \\end{center}
            Nhận thấy đồ thị hàm số đi qua gốc tọa độ $O(0;0)$, đồng thời khi $x = \\frac{\\pi}{2}$ thì $y = -1$ và khi $x = -\\frac{\\pi}{2}$ thì $y = 1$.\\\\
            Giá trị này đối ngược hoàn toàn với hàm số $y = \\sin x$ cơ bản ($\\sin\\frac{\\pi}{2} = 1$). Do đó, đây là đồ thị của hàm số $y = -\\sin x$.''')

            list_vd_2 = [loigiai_vd_1]

            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ########################################################################
            # Vận dụng cao ############################################
            vdc_da_1_d = '\\True Giá trị lớn nhất của hàm số $y = \\sin^2 x - \\cos x + %s$ là $\\frac{%s}{4}$' % (latex(m_val), latex(max_val_frac.numerator))
            vdc_da_1_s = 'Giá trị lớn nhất của hàm số $y = \\sin^2 x - \\cos x + %s$ là $\\frac{%s}{4}$' % (latex(m_val), latex(max_val_sai_frac.numerator))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            list_vdc_1 = [vdc_da_1]

            loigiai_vdc_1 = ('''Biến đổi hàm số về dạng đa thức bậc hai đối với $\\cos x$:\\\\
            $y = (1 - \\cos^2 x) - \\cos x + %s = -\\cos^2 x - \\cos x + %s$.\\\\
            Đặt $t = \\cos x$ với điều kiện $t \\in [-1; 1]$, hàm số trở thành: $f(t) = -t^2 - t + %s$.\\\\
            Xét hàm số bậc hai trên đoạn $[-1; 1]$, đồ thị hàm số là một parabol có bề lõm quay xuống dưới, đỉnh parabol có hoành độ tại điểm $t = -\\frac{1}{2} \\in [-1; 1]$.\\\\
            Do đó, giá trị lớn nhất của hàm số đạt được tại điểm đỉnh:\\\\
            $\\max y = f\\left( -\\frac{1}{2} \\right) = -\\left( -\\frac{1}{2} \\right)^2 - \\left( -\\frac{1}{2} \\right) + %s = -\\frac{1}{4} + \\frac{1}{2} + %s = \\frac{1}{4} + %s = \\frac{%s}{4}$.''' 
                             % (latex(m_val), latex(m_val + 1), latex(m_val + 1), latex(m_val + 1), latex(m_val + 1), latex(m_val + 1), latex(max_val_frac.numerator)))

            list_vdc_2 = [loigiai_vdc_1]

            combined_vdc = list(zip(list_vdc_1, list_vdc_2))
            random.shuffle(combined_vdc)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)


            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Lặp đến khi đáp án tổng hợp có từ 1 đến 3 đúng
            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)

                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                true_count = count_true_answers(answers)

                if 1 <= true_count <= 3:
                    break

            # Gán lại vào list sau khi kiểm tra xong điều kiện vòng lặp
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

            # Xuất câu hỏi và đáp án kết hợp lời giải chi tiết đã được xáo trộn qua định dạng %s
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+
            str(noidungcauhoi)+ 
                '\\choiceTFn \n'
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
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

