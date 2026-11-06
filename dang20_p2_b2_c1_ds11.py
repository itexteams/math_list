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


def bt_dang20_p2_b2_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến không gian
            x = symbols('x')

            # Thiết lập bộ chọn ngẫu nhiên bài toán để đa dạng hóa câu hỏi (1: Bài gốc, 2: Bài biến thể)
            kieu_bo = random.choice([1, 2])

            if kieu_bo == 1:
                goc_tong_latex = '\\frac{\\pi}{4}'
                tich_latex = '3 - 2\\sqrt{2}'

                # tan a + tan b = 1 - (3 - 2sqrt(2)) = -2 + 2sqrt(2)
                tong_dung_latex = '-2 + 2\\sqrt{2}'
                tong_sai_latex = '2 - 2\\sqrt{2}'

                # Do tan a tan b = (-1 + sqrt(2))^2 và tan a + tan b = 2(-1 + sqrt(2)) nên tan a = tan b = -1 + sqrt(2)
                tana_dung_latex = '-1 + \\sqrt{2}'
                tana_sai_latex = '1 - \\sqrt{2}'

                tanb_dung_latex = '-1 + \\sqrt{2}'
                tanb_sai_latex = '-1 - \\sqrt{2}'

                # tan a - tan b = 0
                hieu_dung_latex = '0'
                hieu_sai_latex = '-2 - 2\\sqrt{2}'

                loigiai_tính_toán = ('''Ta có $\\tan(a+b) = \\tan\\frac{\\pi}{4} = 1$.\\\\'''
                                     '''Mặt khác, theo công thức cộng ta có: $\\tan(a+b) = \\frac{\\tan a + \\tan b}{1 - \\tan a \\tan b} = 1 \\\\ \\Rightarrow \\tan a + \\tan b = 1 - \\tan a \\tan b$.\\\\'''
                                     '''Thay giả thiết $\\tan a \\tan b = 3 - 2\\sqrt{2}$ vào, ta được:\\\\'''
                                     '''$\\tan a + \\tan b = 1 - (3 - 2\\sqrt{2}) = -2 + 2\\sqrt{2}$.\\\\'''
                                     '''Theo định lý Vi-ét đảo, $\\tan a$ và $\\tan b$ là hai nghiệm của phương trình:\\\\'''
                                     '''$X^2 - (-2 + 2\\sqrt{2})X + (3 - 2\\sqrt{2}) = 0 \\Leftrightarrow \\left[X - (-1 + \\sqrt{2})\\right]^2 = 0 \\Leftrightarrow X = -1 + \\sqrt{2}$.\\\\'''
                                     '''Do đó $\\tan a = \\tan b = -1 + \\sqrt{2}$.\\\\'''
                                     '''Suy ra hiệu $\\tan a - \\tan b = 0$.''')
            else:
                goc_tong_latex = '\\frac{\\pi}{3}'
                tich_latex = '2 - \\sqrt{3}'

                # tan(a+b) = sqrt(3) => tan a + tan b = sqrt(3)(1 - (2 - sqrt(3))) = sqrt(3)(sqrt(3) - 1) = 3 - sqrt(3)
                tong_dung_latex = '3 - \\sqrt{3}'
                tong_sai_latex = '3 + \\sqrt{3}'

                # Phương trình: X^2 - (3 - sqrt(3))X + (2 - sqrt(3)) = 0 có nghiệm X = 1 và X = 2 - sqrt(3)
                # Vì 0 < a,b < pi/2 và a+b = pi/3 nên giả sử tan a = 1, tan b = 2 - sqrt(3)
                tana_dung_latex = '1'
                tana_sai_latex = '\\sqrt{3}'

                tanb_dung_latex = '2 - \\sqrt{3}'
                tanb_sai_latex = '2 + \\sqrt{3}'

                # tan a - tan b = 1 - (2 - sqrt(3)) = -1 + sqrt(3)
                hieu_dung_latex = '-1 + \\sqrt{3}'
                hieu_sai_latex = '1 - \\sqrt{3}'

                loigiai_tính_toán = ('''Ta có $\\tan(a+b) = \\tan\\frac{\\pi}{3} = \\sqrt{3}$.\\\\'''
                                     '''Mặt khác, theo công thức cộng ta có: $\\tan(a+b) = \\frac{\\tan a + \\tan b}{1 - \\tan a \\tan b} = \\sqrt{3} \\\\ \\Rightarrow \\tan a + \\tan b = \\sqrt{3}(1 - \\tan a \\tan b)$.\\\\'''
                                     '''Thay giả thiết $\\tan a \\tan b = 2 - \\sqrt{3}$ vào, ta được:\\\\'''
                                     '''$\\tan a + \\tan b = \\sqrt{3}\\left[1 - (2 - \\sqrt{3})\\right] = \\sqrt{3}(\\sqrt{3} - 1) = 3 - \\sqrt{3}$.\\\\'''
                                     '''Theo định lý Vi-ét đảo, $\\tan a$ và $\\tan b$ là hai nghiệm của phương trình:\\\\'''
                                     '''$X^2 - (3 - \\sqrt{3})X + (2 - \\sqrt{3}) = 0 \\Leftrightarrow (X - 1)\\left[X - (2 - \\sqrt{3})\\right] = 0$.\\\\'''
                                     '''Do vai trò đối xứng, ta có thể chọn $\\tan a = 1$ và $\\tan b = 2 - \\sqrt{3}$.\\\\'''
                                     '''Suy ra hiệu $\\tan a - \\tan b = 1 - (2 - \\sqrt{3}) = -1 + \\sqrt{3}$.''')

            # Nội dung câu hỏi chính sử dụng %s
            noidungcauhoi = ('''Biết $0 < a,b < \\frac{\\pi}{2}, a+b = %s$ và $\\tan a \\tan b = %s$. Xác định tính đúng, sai của các khẳng định''' 
                             %(goc_tong_latex, tich_latex))

            ########################################################################
            # Nhận biết (Khẳng định về tổng) ############################################
            nb_da_1_d = '\\True $\\tan a + \\tan b = %s$' %(tong_dung_latex)
            nb_da_1_s = '$\\tan a + \\tan b = %s$' %(tong_sai_latex)
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            list_nb_1 = [nb_da_1]
            loigiai_nb_1 = ('''Dựa vào biểu thức biến đổi của công thức cộng lượng giác cho $\\tan(a+b)$, ta thu được giá trị của tổng $\\tan a + \\tan b = %s$.''' %(tong_dung_latex))
            list_nb_2 = [loigiai_nb_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu (Khẳng định về tan a) ############################################
            th_da_1_d = '\\True $\\tan a = %s$' %(tana_dung_latex)
            th_da_1_s = '$\\tan a = %s$' %(tana_sai_latex)
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            list_th_1 = [th_da_1]
            loigiai_th_1 = ('''Từ phương trình bậc hai xác định nghiệm hệ thức Vi-ét, ta tìm được giá trị nghiệm phù hợp cho $\\tan a = %s$.''' %(tana_dung_latex))
            list_th_2 = [loigiai_th_1]

            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## 
            # Vận dụng (Khẳng định về tan b) ############################################
            vd_da_1_d = '\\True $\\tan b = %s$' %(tanb_dung_latex)
            vd_da_1_s = '$\\tan b = %s$' %(tanb_sai_latex)
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            list_vd_1 = [vd_da_1]
            loigiai_vd_1 = ('''Tương tự, giá trị của $\\tan b$ nhận giá trị nghiệm còn lại tương ứng là $\\tan b = %s$. Khẳng định sai lệch hằng số dấu của căn thức là khẳng định sai.''' %(tanb_dung_latex))
            list_vd_2 = [loigiai_vd_1]

            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## 
            # Vận dụng cao (Khẳng định về hiệu) ############################################
            vdc_da_1_d = '\\True $\\tan a - \\tan b = %s$' %(hieu_dung_latex)
            vdc_da_1_s = '$\\tan a - \\tan b = %s$' %(hieu_sai_latex)
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            list_vdc_1 = [vdc_da_1]
            loigiai_vdc_1 = ('''Kết hợp toàn bộ các bước tính toán chi tiết:\\\\ %s''' %(loigiai_tính_toán))
            list_vdc_2 = [loigiai_vdc_1]

            combined_vdc = list(zip(list_vdc_1, list_vdc_2))
            random.shuffle(combined_vdc)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Vòng lặp kiểm tra để đảm bảo số lượng đáp án đúng nằm trong khoảng từ 1 đến 3
            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)

                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                true_count = count_true_answers(answers)

                if 1 <= true_count <= 3:
                    break

            # Thiết lập lại danh sách đồng bộ sau khi lọc thỏa mãn điều kiện
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

            # Xuất dữ liệu câu hỏi và lời giải chi tiết theo đúng định dạng %s của khung chương trình mẫu
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

