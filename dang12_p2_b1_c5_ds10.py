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


def bt_dang12_p2_b1_c5_ds10(self):
            # Khai báo biến
            # n1: bi đỏ, n2: bi xanh, n3: bi vàng
            n1 = randint(6, 8)
            n2 = randint(8, 10)
            n3 = randint(4, 6)
            tong_bi = n1 + n2 + n3

            # Các giá trị tính toán
            cach_3_mau = n1 * n2 * n3
            cach_do_xanh = n1 * n2
            cach_do_vang = n1 * n3
            cach_xanh_vang = n2 * n3
            cach_2_mau_tong = cach_do_xanh + cach_do_vang + cach_xanh_vang

            # Nội dung câu hỏi
            noidungcauhoi = ('''Một túi có %s viên bi khác nhau trong đó có %s bi đỏ, %s bi xanh và %s bi vàng.''' 
                             %(latex(tong_bi), latex(n1), latex(n2), latex(n3)))

            ########################################################################
            # Nhận biết - Câu (a): Chọn 3 bi khác màu
            ########################################################################
            nb_da_1_d = '\\True Số cách chọn ba bi khác màu là %s (cách)' %(latex(cach_3_mau))
            nb_da_1_s = 'Số cách chọn ba bi khác màu là %s (cách)' %(latex(cach_3_mau + randint(5, 15)))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = ('''Để chọn được ba viên bi khác màu, ta phải chọn mỗi màu một viên bi. \\\\
                            Số cách chọn $1$ bi đỏ là %s cách. \\\\
                            Số cách chọn $1$ bi xanh là %s cách. \\\\
                            Số cách chọn $1$ bi vàng là %s cách. \\\\
                            Theo quy tắc nhân, số cách chọn ba bi khác màu là: $%s \\cdot %s \\cdot %s = %s$ cách.''' 
                            %(latex(n1), latex(n2), latex(n3), latex(n1), latex(n2), latex(n3), latex(cach_3_mau)))

            list_nb_1 = [nb_da_1]
            list_nb_2 = [loigiai_nb_1]
            combined_nb = list(zip(list_nb_1, list_nb_2))

            ########################################################################
            # Thông hiểu - Câu (b): Chọn 2 bi đỏ và xanh
            ########################################################################
            th_da_1_d = '\\True Số cách chọn hai viên khác màu bi đỏ và bi xanh là %s (cách)' %(latex(cach_do_xanh))
            th_da_1_s = 'Số cách chọn hai viên khác màu bi đỏ và bi xanh là %s (cách)' %(latex(n1 + n2))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = ('''Số cách chọn một viên bi đỏ là %s cách. \\\\
                            Số cách chọn một viên bi xanh là %s cách. \\\\
                            Số cách chọn hai viên bi gồm một đỏ và một xanh là: $%s \\cdot %s = %s$ cách.''' 
                            %(latex(n1), latex(n2), latex(n1), latex(n2), latex(cach_do_xanh)))

            list_th_1 = [th_da_1]
            list_th_2 = [loigiai_th_1]
            combined_th = list(zip(list_th_1, list_th_2))

            ########################################################################
            # Vận dụng - Câu (c): Chọn 2 bi đỏ và vàng
            ########################################################################
            vd_da_1_d = '\\True Số cách chọn hai viên khác màu bi đỏ và bi vàng là %s (cách)' %(latex(cach_do_vang))
            vd_da_1_s = 'Số cách chọn hai viên khác màu bi đỏ và bi vàng là %s (cách)' %(latex(cach_do_vang + 5))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = ('''Số cách chọn một viên bi đỏ là %s cách. \\\\
                            Số cách chọn một viên bi vàng là %s cách. \\\\
                            Số cách chọn hai viên bi gồm một đỏ và một vàng là: $%s \\cdot %s = %s$ cách.''' 
                            %(latex(n1), latex(n3), latex(n1), latex(n3), latex(cach_do_vang)))

            list_vd_1 = [vd_da_1]
            list_vd_2 = [loigiai_vd_1]
            combined_vd = list(zip(list_vd_1, list_vd_2))

            ########################################################################
            # Vận dụng cao - Câu (d): Chọn 2 bi khác màu (tổng quát)
            ########################################################################
            vdc_da_1_d = '\\True Số cách chọn hai bi khác màu là: %s (cách)' %(latex(cach_2_mau_tong))
            vdc_da_1_s = 'Số cách chọn hai bi khác màu là: %s (cách)' %(latex(cach_do_xanh + cach_do_vang))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = ('''Để chọn hai bi khác màu, ta có các trường hợp sau: \\\\
                            Trường hợp 1: Chọn $1$ đỏ và $1$ xanh có $%s \\cdot %s = %s$ cách. \\\\
                            Trường hợp 2: Chọn $1$ đỏ và $1$ vàng có $%s \\cdot %s = %s$ cách. \\\\
                            Trường hợp 3: Chọn $1$ xanh và $1$ vàng có $%s \\cdot %s = %s$ cách. \\\\
                            Vậy tổng số cách chọn hai bi khác màu là: $%s + %s + %s = %s$ cách.''' 
                             %(latex(n1), latex(n2), latex(cach_do_xanh), 
                               latex(n1), latex(n3), latex(cach_do_vang),
                               latex(n2), latex(n3), latex(cach_xanh_vang),
                               latex(cach_do_xanh), latex(cach_do_vang), latex(cach_xanh_vang), latex(cach_2_mau_tong)))

            list_vdc_1 = [vdc_da_1]
            list_vdc_2 = [loigiai_vdc_1]
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Lặp đến khi đáp án có từ 1 đến 3 đúng
            while True:
                nb_sel = random.choice(combined_nb)
                th_sel = random.choice(combined_th)
                vd_sel = random.choice(combined_vd)
                vdc_sel = random.choice(combined_vdc)

                answers = [nb_sel[0], th_sel[0], vd_sel[0], vdc_sel[0]]
                true_count = count_true_answers(answers)

                if 1 <= true_count <= 3:
                    shuffled_answers = [nb_sel[0], th_sel[0], vd_sel[0], vdc_sel[0]]
                    shuffled_solutions = [nb_sel[1], th_sel[1], vd_sel[1], vdc_sel[1]]
                    break

            # Xuất câu hỏi
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+
                str(noidungcauhoi)+ 
                '\\choiceTFn \n'
                '{'+str(shuffled_answers[0])+'}\n'
                '{'+str(shuffled_answers[1])+'}\n'
                '{'+str(shuffled_answers[2])+'}\n'
                '{'+str(shuffled_answers[3])+'}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(shuffled_solutions[0])+'\n'
                '\\item '+str(shuffled_solutions[1])+'\n'
                '\\item '+str(shuffled_solutions[2])+'\n'
                '\\item '+str(shuffled_solutions[3])+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

