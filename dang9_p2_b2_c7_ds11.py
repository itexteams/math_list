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


def bt_dang9_p2_b2_c7_ds11(self):
            # Khai báo biến
            # Khai báo biến và hàm số
            t = symbols('t')
            # Random các hệ số cho phương trình s(t) = at^3 + bt^2 + ct + d
            # Để số đẹp, ta thường lấy a=1, b âm, c và d dương.
            a = 1
            b = randint(-4, -2)
            c = randint(4, 6)
            d = randint(1, 5)

            st = a*t**3 + b*t**2 + c*t + d
            vt = diff(st, t)
            at_acc = diff(vt, t)

            # Nội dung câu hỏi
            noidungcauhoi = ('''Một chất điểm chuyển động thẳng được xác định bởi phương trình: $s\\left( t \\right) = %s$, trong đó $t$ tính bằng giây và $s$ tính bằng mét.''' 
                             %(latex(st)))

            ########################################################################
            # Nhận biết: Tính quãng đường tại thời điểm t1
            t1 = 3
            s_t1 = st.subs(t, t1)
            s_t1_wrong = s_t1 + randint(2, 5)

            nb_da_1_d = '\\True Quãng đường tại thời điểm $%s$ giây là $%s m$' %(latex(t1), latex(s_t1))
            nb_da_1_s = 'Quãng đường tại thời điểm $%s$ giây là $%s m$' %(latex(t1), latex(s_t1_wrong))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)
            list_nb_1 = [nb_da_1]

            loigiai_nb_1 = ('''Thay $t = %s$ vào phương trình quãng đường, ta được:\\\\ $s\\left( %s \\right) = %s^3 %s \\cdot %s^2 + %s \\cdot %s + %s = %s$.'''
                        %(latex(t1), latex(t1), latex(t1), latex(b), latex(t1), latex(c), latex(t1), latex(d), latex(s_t1)))
            list_nb_2 = [loigiai_nb_1]

            ########################################################################
            # Thông hiểu: Tính vận tốc tại thời điểm t2
            t2 = 4
            v_t2 = vt.subs(t, t2)
            v_t2_wrong = v_t2 - randint(2, 4)

            th_da_1_d = '\\True Vận tốc của chất điểm tại thời điểm $%s$ giây là: $%s \\left( m/s \\right)$' %(latex(t2), latex(v_t2))
            th_da_1_s = 'Vận tốc của chất điểm tại thời điểm $%s$ giây là: $%s \\left( m/s \\right)$' %(latex(t2), latex(v_t2_wrong))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)
            list_th_1 = [th_da_1]

            loigiai_th_1 = ('''Vận tốc của chất điểm là $v\\left( t \\right) = s\'\\left( t \\right) = %s$.\\\\ Tại thời điểm $t = %s$, vận tốc là $v\\left( %s \\right) = 3 \\cdot %s^2 %s \\cdot %s + %s = %s$.''' 
                       %(latex(vt), latex(t2), latex(t2), latex(t2), latex(2*b), latex(t2), latex(c), latex(v_t2)))
            list_th_2 = [loigiai_th_1]

            ########################################################################
            # Vận dụng: Gia tốc tại thời điểm t3
            t3 = 1
            a_t3 = at_acc.subs(t, t3)
            a_t3_wrong = a_t3 + randint(1, 3)

            vd_da_1_d = '\\True Tại thời điểm $t = %s \\left( s \\right)$ thì gia tốc của chất điểm bằng $%s$' %(latex(t3), latex(a_t3))
            vd_da_1_s = 'Tại thời điểm $t = %s \\left( s \\right)$ thì gia tốc của chất điểm bằng $%s$' %(latex(t3), latex(a_t3_wrong))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)
            list_vd_1 = [vd_da_1]

            loigiai_vd_1 = ('''Gia tốc của chất điểm là $a\\left( t \\right) = v\'\\left( t \\right) = %s$.\\\\ Tại thời điểm $t = %s$, gia tốc là $a\\left( %s \\right) = 6 \\cdot %s %s = %s$.'''
                       %(latex(at_acc), latex(t3), latex(t3), latex(t3), latex(2*b), latex(a_t3)))
            list_vd_2 = [loigiai_vd_1]

            ########################################################################
            # Vận dụng cao: Quãng đường trong khoảng thời gian [t4, t5]
            t4 = 2
            t5 = 5
            dist = st.subs(t, t5) - st.subs(t, t4)
            dist_wrong = dist + randint(5, 10)

            vdc_da_1_d = '\\True Trong khoảng thời gian từ $%s$ giây đến $%s$ giây thì chất điểm chuyển động được $%s m$' %(latex(t4), latex(t5), latex(dist))
            vdc_da_1_s = 'Trong khoảng thời gian từ $%s$ giây đến $%s$ giây thì chất điểm chuyển động được $%s m$' %(latex(t4), latex(t5), latex(dist_wrong))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)
            list_vdc_1 = [vdc_da_1]

            loigiai_vdc_1 = ('''Quãng đường chất điểm đi được từ $t = %s$ đến $t = %s$ là:\\\\ $\\Delta s = s\\left( %s \\right) - s\\left( %s \\right) = %s - %s = %s$.'''
                       %(latex(t5), latex(t4), latex(t5), latex(t4), latex(st.subs(t, t5)), latex(st.subs(t, t4)), latex(dist)))
            list_vdc_2 = [loigiai_vdc_1]

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

            # Gán lại vào list để xáo trộn (trong bài này mỗi list chỉ có 1 phần tử đã chọn)
            list_nb_1 = [nb_da_1]
            list_th_1 = [th_da_1]
            list_vd_1 = [vd_da_1]
            list_vdc_1 = [vdc_da_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            combined_th = list(zip(list_th_1, list_th_2))
            combined_vd = list(zip(list_vd_1, list_vd_2))
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))

            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            # Xuất câu hỏi
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

