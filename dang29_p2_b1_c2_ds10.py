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


def bt_dang29_p2_b1_c2_ds10(self):
            # Khai báo biến
            # Khai báo biến
            x, y = symbols('x y')

            # Random thông số
            # pck: phí xe ô tô (đơn vị: nghìn đồng)
            pck = random.choice([10, 15, 20, 25, 30])
            # kt: tỉ lệ phí xe tải / xe ô tô (số nguyên)
            kt = random.randint(2, 4)
            # ptk: phí xe tải (đơn vị: nghìn đồng)
            ptk = pck * kt
            # kM: tổng phí chia cho pck
            kM = random.randint(30, 80)
            # Mk: tổng phí tối thiểu (đơn vị: nghìn đồng)
            Mk = pck * kM

            # Chuyển sang đơn vị đồng
            pc_val = pck * 1000
            pt_val = ptk * 1000
            M_val = Mk * 1000

            # Tính số lượng tối thiểu cho câu d
            n_min_float = kM / (1 + kt)
            n_min = math.ceil(n_min_float)

            n_min_false = n_min - random.randint(1, 3)
            if n_min_false <= 0:
                n_min_false = n_min + random.randint(1, 3)

            # Bước biến đổi để in ra lời giải VDC
            if kM % (1 + kt) == 0:
                ineq_step = "x \\ge %s" % (n_min)
            else:
                ineq_step = "x \\ge \\frac{%s}{%s} \\approx %s" % (kM, 1 + kt, str(round(n_min_float, 2)).replace('.', ','))

            # Nội dung câu hỏi
            noidungcauhoi = ('''Có $x$ cái ô tô và $y$ cái xe tải ở bãi đỗ xe. Phí gửi xe ô tô là $%s$ đồng và xe tải là $%s$ đồng. Biết rằng, sáng thứ Ba tổng cộng tiền phí gửi xe thu được tối thiểu $%s$ đồng.'''                  
                             % (pc_val, pt_val, M_val))

            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Số tiền phí gửi của $x$ chiếc ô tô là $%sx$ nghìn đồng' % (pck)
            nb_da_1_s = 'Số tiền phí gửi của $x$ chiếc ô tô là $%sx$ nghìn đồng' % (ptk)

            loigiai_nb_d = ('''Phí gửi một chiếc ô tô là $%s$ đồng = $%s$ nghìn đồng. \\\\ 
            Số tiền phí gửi của $x$ chiếc ô tô là $%sx$ nghìn đồng. \\\\ 
            Mệnh đề đúng.''' % (pc_val, pck, pck))

            loigiai_nb_s = ('''Phí gửi một chiếc ô tô là $%s$ đồng = $%s$ nghìn đồng. \\\\ 
            Số tiền phí gửi của $x$ chiếc ô tô là $%sx$ nghìn đồng. \\\\ 
            Mệnh đề sai.''' % (pc_val, pck, pck))

            ######################################################################## Thông hiểu ############################################
            # Các đáp án
            th_da_1_d = '\\True Tổng số tiền phí gửi xe thu được là $%sx+%sy$ nghìn đồng' % (pck, ptk)
            th_da_1_s = 'Tổng số tiền phí gửi xe thu được là $%sx+%sy$ nghìn đồng' % (ptk, pck)

            loigiai_th_d = ('''Phí gửi xe ô tô là $%s$ nghìn đồng, xe tải là $%s$ nghìn đồng. \\\\
            Tổng số tiền phí gửi xe ô tô và xe tải thu được là $%sx + %sy$ nghìn đồng. \\\\
            Mệnh đề đúng.''' % (pck, ptk, pck, ptk))

            loigiai_th_s = ('''Phí gửi xe ô tô là $%s$ nghìn đồng, xe tải là $%s$ nghìn đồng. \\\\
            Tổng số tiền phí gửi xe ô tô và xe tải thu được là $%sx + %sy$ nghìn đồng. \\\\
            Mệnh đề sai.''' % (pck, ptk, pck, ptk))

            ######################################################################## Vận dụng ############################################
            # Các đáp án
            vd_da_1_s = 'Bất phương trình biểu thị số tiền gửi xe của sáng thứ Ba là $x+%sy \\le %s$' % (kt, kM)
            vd_da_1_d = '\\True Bất phương trình biểu thị số tiền gửi xe của sáng thứ Ba là $x+%sy \\ge %s$' % (kt, kM)

            loigiai_vd_d = ('''Vì tổng số tiền phí gửi xe thu được tối thiểu là $%s$ đồng = $%s$ nghìn đồng nên ta có bất phương trình: \\\\
            $%sx + %sy \\ge %s \\Leftrightarrow x + %sy \\ge %s$. \\\\
            Mệnh đề đúng.''' % (M_val, Mk, pck, ptk, Mk, kt, kM))

            loigiai_vd_s = ('''Vì tổng số tiền phí gửi xe thu được tối thiểu là $%s$ đồng = $%s$ nghìn đồng nên ta có bất phương trình: \\\\
            $%sx + %sy \\ge %s \\Leftrightarrow x + %sy \\ge %s$. \\\\
            Mệnh đề sai.''' % (M_val, Mk, pck, ptk, Mk, kt, kM))

            ######################################################################## Vận dụng cao ############################################
            # Các đáp án
            vdc_da_1_d = '\\True Nếu số xe ô tô và số xe tải gửi sáng thứ Ba bằng nhau, thì ít nhất mỗi loại có $%s$ chiếc gửi ở bãi đỗ xe này' % (n_min)
            vdc_da_1_s = 'Nếu số xe ô tô và số xe tải gửi sáng thứ Ba bằng nhau, thì ít nhất mỗi loại có $%s$ chiếc gửi ở bãi đỗ xe này' % (n_min_false)

            loigiai_vdc_d = ('''Vì số xe ô tô và xe tải bằng nhau nên $x = y$. \\\\
            Thay vào bất phương trình $x + %sy \\ge %s$ ta được: \\\\
            $x + %sx \\ge %s \\Leftrightarrow %sx \\ge %s \\Leftrightarrow %s$. \\\\
            Vì $x$ là số nguyên dương nên ít nhất mỗi loại có $%s$ chiếc gửi ở bãi đỗ xe này. \\\\
            Mệnh đề đúng.''' % (kt, kM, kt, kM, 1+kt, kM, ineq_step, n_min))

            loigiai_vdc_s = ('''Vì số xe ô tô và xe tải bằng nhau nên $x = y$. \\\\
            Thay vào bất phương trình $x + %sy \\ge %s$ ta được: \\\\
            $x + %sx \\ge %s \\Leftrightarrow %sx \\ge %s \\Leftrightarrow %s$. \\\\
            Vì $x$ là số nguyên dương nên ít nhất mỗi loại có $%s$ chiếc gửi ở bãi đỗ xe này. \\\\
            Mệnh đề sai.''' % (kt, kM, kt, kM, 1+kt, kM, ineq_step, n_min))


            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Gom nhóm phương án và lời giải để đồng bộ logic khi xáo trộn
            list_nb = [(nb_da_1_d, loigiai_nb_d), (nb_da_1_s, loigiai_nb_s)]
            list_th = [(th_da_1_d, loigiai_th_d), (th_da_1_s, loigiai_th_s)]
            list_vd = [(vd_da_1_d, loigiai_vd_d), (vd_da_1_s, loigiai_vd_s)]
            list_vdc = [(vdc_da_1_d, loigiai_vdc_d), (vdc_da_1_s, loigiai_vdc_s)]

            # Lặp đến khi đáp án có từ 1 đến 3 đúng
            while True:
                nb = random.choice(list_nb)
                th = random.choice(list_th)
                vd = random.choice(list_vd)
                vdc = random.choice(list_vdc)

                answers = [nb[0], th[0], vd[0], vdc[0]]
                true_count = count_true_answers(answers)

                if 1 <= true_count <= 3:
                    break

            # Gán lại vào list (Đảm bảo câu hỏi đi kèm đúng với lời giải tương ứng)
            list_nb_1 = [nb[0]]
            list_nb_2 = [nb[1]]

            list_th_1 = [th[0]]
            list_th_2 = [th[1]]

            list_vd_1 = [vd[0]]
            list_vd_2 = [vd[1]]

            list_vdc_1 = [vdc[0]]
            list_vdc_2 = [vdc[1]]

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
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

