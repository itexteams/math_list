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


def bt_dang21_p2_b1_c1_ds11(self):
            # Khai báo biến
            # Chọn ngẫu nhiên bộ số đẹp cho cot a = ts / ms
            cot_pairs = [(7, 3), (4, 3), (12, 5), (2, 1), (3, 2)]
            ts, ms = random.choice(cot_pairs)

            cot_val = Rational(ts, ms)
            tan_val = Rational(ms, ts)
            binh_phuong_tong = ts**2 + ms**2

            # Tính toán các giá trị chính xác bằng SymPy
            sin_a_correct = -ms / sqrt(binh_phuong_tong)
            tan_c_correct = -cot_val

            # Tính giá trị biểu thức câu d (thay x bằng a)
            # P = (tan^3 a + 2) / [ (2tan a + 3cos a/cos a) * cos^2 a ] -> Chia tử mẫu cho cos^3 a
            # Tử = tan^3 a + 2
            # Mẫu = (2sin a + 3cos a) * (1 + tan^2 a)
            tu_d = tan_val**3 + 2
            mau_d = (2*tan_val + 3) * (1 + tan_val**2)
            val_d_correct = tu_d / mau_d

            # Nội dung câu hỏi
            noidungcauhoi = ('''Biết $\\cot a = \\frac{%s}{%s}$ và $\\pi < a < \\frac{3\\pi}{2}$. Xét tính đúng sai của các mệnh đề sau:''' %(latex(ts), latex(ms)))

            ########################################################################
            # Nhận biết ############################################
            # Câu a (Mẫu gốc: Sai)
            nb_da_1_s = '$\\tan (a + \\pi) = -\\frac{%s}{%s}$' %(latex(ms), latex(ts))
            nb_da_1_d = '\\True $\\tan (a + \\pi) = \\frac{%s}{%s}$' %(latex(ms), latex(ts))
            list_nb_da_1 = [nb_da_1_s, nb_da_1_d]
            nb_da_1 = random.choice(list_nb_da_1)

            list_nb_1 = [nb_da_1]

            loigiai_nb_1 = ('''Ta có $\\tan (a + \\pi) = \\tan a = \\frac{1}{\\cot a} = \\frac{%s}{%s}$.''' %(latex(ms), latex(ts)))
            list_nb_2 = [loigiai_nb_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu ############################################
            # Câu b (Mẫu gốc: Đúng)
            th_da_1_d = '\\True $\\sin (\\pi - a) = %s$' %(latex(sin_a_correct))
            th_da_1_s = '$\\sin (\\pi - a) = %s$' %(latex(-sin_a_correct))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            list_th_1 = [th_da_1]

            loigiai_th_1 = ('''Ta có $\\sin (\\pi - a) = \\sin a$.\\\\
            Vì $\\pi < a < \\frac{3\\pi}{2}$ nên $\\sin a < 0$.\\\\
            Mặt khác $1 + \\cot^2 a = \\frac{1}{\\sin^2 a} \\Rightarrow \\sin^2 a = \\frac{1}{1 + \\left(\\frac{%s}{%s}\\right)^2} = \\frac{%s}{%s}$.\\\\
            Do đó $\\sin a = %s$.''' %(latex(ts), latex(ms), latex(ms**2), latex(binh_phuong_tong), latex(sin_a_correct)))
            list_th_2 = [loigiai_th_1]

            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## 
            # Vận dụng ############################################
            # Câu c (Mẫu gốc: Sai)
            vd_da_1_s = '$\\tan \\left(a - \\frac{11\\pi}{2}\\right) = \\frac{%s}{%s}$' %(latex(ms), latex(ts))
            vd_da_1_d = '\\True $\\tan \\left(a - \\frac{11\\pi}{2}\\right) = %s$' %(latex(tan_c_correct))
            list_vd_da_1 = [vd_da_1_s, vd_da_1_d]
            vd_da_1 = random.choice(list_vd_da_1)

            list_vd_1 = [vd_da_1]

            loigiai_vd_1 = ('''Ta có $\\tan \\left(a - \\frac{11\\pi}{2}\\right) = \\tan \\left(a - \\frac{\\pi}{2} - 5\\pi\\right) = \\tan \\left(a - \\frac{\\pi}{2}\\right) = -\\cot a = -\\frac{%s}{%s}$.''' %(latex(ts), latex(ms)))
            list_vd_2 = [loigiai_vd_1]

            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## 
            # Vận dụng cao ############################################
            # Câu d (Mẫu gốc: Đúng)
            vdc_da_1_d = '\\True $\\frac{\\sin^3 a + 2\\cos^3 a}{2\\sin a + 3\\cos a} = %s$' %(latex(val_d_correct))
            vdc_da_1_s = '$\\frac{\\sin^3 a + 2\\cos^3 a}{2\\sin a + 3\\cos a} = \\frac{1}{2}$'
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            list_vdc_1 = [vdc_da_1]

            loigiai_vdc_1 = ('''Chia cả tử và mẫu của biểu thức cho $\\cos^3 a$, ta được:\\\\
            $\\frac{\\tan^3 a + 2}{\\frac{2\\sin a + 3\\cos a}{\\cos^3 a}} = \\frac{\\tan^3 a + 2}{(2\\tan a + 3)\\frac{1}{\\cos^2 a}} = \\frac{\\tan^3 a + 2}{(2\\tan a + 3)(1 + \\tan^2 a)}$.\\\\
            Thay $\\tan a = \\frac{%s}{%s}$ vào biểu thức, ta tính được giá trị bằng $%s$.''' %(latex(ms), latex(ts), latex(val_d_correct)))
            list_vdc_2 = [loigiai_vdc_1]

            combined_vdc = list(zip(list_vdc_1, list_vdc_2))
            random.shuffle(combined_vdc)
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
            str(noidungcauhoi)+ '\n'
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

