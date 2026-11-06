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


def bt_dang29_p2_b4_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # B3-Suy nghĩ tìm cách random bài toán
            # Random hệ số góc 'a' của phương trình sin(a*x) = m
            a_goc = random.choice([2, 3])

            if a_goc == 2:
                str_pt_goc = "\\sin 2x = m"
                str_nghiem_a = "x = \\frac{k\\pi}{2}"
                loigiai_a_bai = "2x = k\\pi \\Leftrightarrow x = \\frac{k\\pi}{2}"

                # Câu b: thử x = pi/3 => sin(2*pi/3) = sqrt(3)/2
                str_x_b = "\\frac{\\pi}{3}"
                str_m_b_sai = "\\frac{-1}{2}"
                str_vt_b = "\\frac{\\sqrt{3}}{2}"

                # Câu d: khoảng (0; pi/2) => 2x in (0; pi) -> có 2 nghiệm khi m in (0; 1)
                str_khoang_d = "\\left( 0; \\frac{\\pi}{2} \\right)"
                str_khoang_2x = "(0; \\pi)"
            else:
                str_pt_goc = "\\sin 3x = m"
                str_nghiem_a = "x = \\frac{k\\pi}{3}"
                loigiai_a_bai = "3x = k\\pi \\Leftrightarrow x = \\frac{k\\pi}{3}"

                # Câu b: thử x = pi/9 => sin(3*pi/9) = sin(pi/3) = sqrt(3)/2
                str_x_b = "\\frac{\\pi}{9}"
                str_m_b_sai = "\\frac{1}{2}"
                str_vt_b = "\\frac{\\sqrt{3}}{2}"

                # Câu d: khoảng (0; pi/3) => 3x in (0; pi) -> có 2 nghiệm khi m in (0; 1)
                str_khoang_d = "\\left( 0; \\frac{\\pi}{3} \\right)"
                str_khoang_2x = "(0; \\pi)"

            # Nội dung câu hỏi dạng %s
            noidungcauhoi = ('''Cho phương trình $%s$.''' % (str_pt_goc))

            ########################################################################
            # Nhận biết ############################################
            nb_da_1_d = '\\True Với $m = 0$, phương trình có nghiệm là $%s$' % (str_nghiem_a)
            nb_da_1_s = 'Với $m = 0$, phương trình có nghiệm là $x = k\\pi$'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            list_nb_1 = [nb_da_1]

            loigiai_nb_1 = ('''Khi $m = 0$, phương trình trở thành: $%s = 0 \\Leftrightarrow %s$ ($k \\in \\mathbb{Z}$).''' 
                            % (str_pt_goc, loigiai_a_bai))

            list_nb_2 = [loigiai_nb_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu ############################################
            th_da_1_s = 'Phương trình có nghiệm là $x = %s$ khi $m = %s$' % (str_x_b, str_m_b_sai)
            th_da_1_d = '\\True Phương trình có nghiệm là $x = %s$ khi $m = %s$' % (str_x_b, str_vt_b)
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            list_th_1 = [th_da_1]

            loigiai_th_1 = ('''Thay $x = %s$ vào vế trái của phương trình, ta có:\\\\ $\\sin\\left( %s \\cdot %s \\right) = %s$.\\\\ Do đó, để phương trình nhận $x = %s$ làm nghiệm thì ta phải có $m = %s$.''' 
                            % (str_x_b, latex(a_goc), str_x_b, str_vt_b, str_x_b, str_vt_b))

            list_th_2 = [loigiai_th_1]

            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ########################################################################
            # Vận dụng ############################################
            vd_da_1_s = 'Phương trình có nghiệm khi $m \\in (-1;1)$'
            vd_da_1_d = '\\True Phương trình có nghiệm khi $m \\in [-1;1]$'
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            list_vd_1 = [vd_da_1]

            loigiai_vd_1 = ('''Theo lý thuyết về phương trình lượng giác cơ bản đối với hàm số sin:\\\\ Phương trình $\\sin u = m$ có nghiệm khi và chỉ khi $-1 \\le m \\le 1 \\Leftrightarrow m \\in [-1;1]$.\\\\ Khẳng định ghi $m \\in (-1;1)$ là thiếu các giá trị biên tại $-1$ và $1$.''')

            list_vd_2 = [loigiai_vd_1]

            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ########################################################################
            # Vận dụng cao ############################################
            vdc_da_1_d = '\\True Phương trình có hai nghiệm phân biệt trên $%s$ khi $m \\in (0;1)$' % (str_khoang_d)
            vdc_da_1_s = 'Phương trình có hai nghiệm phân biệt trên $%s$ khi $m \\in [-1;1]$' % (str_khoang_d)
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            list_vdc_1 = [vdc_da_1]

            loigiai_vdc_1 = ('''Khi $x \\in %s \\Rightarrow %sx \\in %s$.\\\\ Trên khoảng $%s$, đồ thị hàm số sin đi từ giá trị $0$ lên $1$ rồi giảm về $0$.\\\\ Do đó, đường thẳng $y = m$ sẽ cắt đồ thị hàm số tại đúng $2$ điểm phân biệt khi và chỉ khi $0 < m < 1 \\Leftrightarrow m \\in (0;1)$.''' 
                             % (str_khoang_d, latex(a_goc), str_khoang_2x, str_khoang_2x))

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

