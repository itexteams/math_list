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


def bt_dang7_p2_b2_c5_ds10(self):
            # Khai báo biến
            # Khai báo biến số lượng hoa
            n_hong = 5
            n_trang = 4
            n_tong = n_hong + n_trang
            k_chon = 4

            # Tính toán các giá trị toán học
            val_a = math.comb(n_tong, k_chon) # 126
            val_b = math.comb(n_hong, 2) * math.comb(n_trang, 2) # 10 * 6 = 60
            val_c = math.comb(n_hong, 3) * math.comb(n_trang, 1) # 10 * 4 = 40
            # Câu d: Có đủ hai màu (Tổng - 4 hồng - 4 trắng)
            val_d_all_hong = math.comb(n_hong, 4)
            val_d_all_trang = math.comb(n_trang, 4)
            val_d = val_a - val_d_all_hong - val_d_all_trang # 126 - 5 - 1 = 120

            # Nội dung câu hỏi
            noidungcauhoi = ('''Có %s bông hồng, %s bông trắng (mỗi bông đều khác nhau về hình dáng). Một người cần chọn một bó bông gồm %s bông từ số bông này.''' 
                             %(latex(n_hong), latex(n_trang), latex(k_chon)))

            ########################################################################
            # Nhận biết (Câu a)
            ########################################################################
            nb_da_1_d = '\\True Số cách chọn %s bông tùy ý là %s cách' %(latex(k_chon), latex(val_a))
            nb_da_1_s = 'Số cách chọn %s bông tùy ý là 120 cách' %(latex(k_chon))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = ('''Số cách chọn %s bông tùy ý từ %s bông là $C_{%s}^{%s} = %s$.'''
                            %(latex(k_chon), latex(n_tong), latex(n_tong), latex(k_chon), latex(val_a)))

            list_nb_1 = [nb_da_1]
            list_nb_2 = [loigiai_nb_1]
            combined_nb = list(zip(list_nb_1, list_nb_2))

            ########################################################################
            # Thông hiểu (Câu b)
            ########################################################################
            th_da_1_d = '\\True Số cách chọn %s bông mà số bông mỗi màu bằng nhau là %s cách' %(latex(k_chon), latex(val_b))
            th_da_1_s = 'Số cách chọn %s bông mà số bông mỗi màu bằng nhau là 50 cách' %(latex(k_chon))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = ('''Để số bông mỗi màu bằng nhau thì ta chọn 2 bông hồng và 2 bông trắng. \\\\
                            Số cách chọn là $C_{%s}^{2} \\cdot C_{%s}^{2} = %s \\cdot %s = %s$ cách.'''
                            %(latex(n_hong), latex(n_trang), latex(math.comb(n_hong, 2)), latex(math.comb(n_trang, 2)), latex(val_b)))

            list_th_1 = [th_da_1]
            list_th_2 = [loigiai_th_1]
            combined_th = list(zip(list_th_1, list_th_2))

            ########################################################################
            # Vận dụng (Câu c)
            ########################################################################
            vd_da_1_d = '\\True Số cách chọn %s bông, trong đó có 3 bông hồng và 1 bông trắng là: %s cách' %(latex(k_chon), latex(val_c))
            vd_da_1_s = 'Số cách chọn %s bông, trong đó có 3 bông hồng và 1 bông trắng là: 30 cách' %(latex(k_chon))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = ('''Số cách chọn 3 bông hồng là $C_{%s}^{3}$ cách. \\\\
                            Số cách chọn 1 bông trắng là $C_{%s}^{1}$ cách. \\\\
                            Số cách chọn thỏa mãn yêu cầu là $C_{%s}^{3} \\cdot C_{%s}^{1} = %s \\cdot %s = %s$ cách.'''
                            %(latex(n_hong), latex(n_trang), latex(n_hong), latex(n_trang), latex(math.comb(n_hong, 3)), latex(math.comb(n_trang, 1)), latex(val_c)))

            list_vd_1 = [vd_da_1]
            list_vd_2 = [loigiai_vd_1]
            combined_vd = list(zip(list_vd_1, list_vd_2))

            ########################################################################
            # Vận dụng cao (Câu d)
            ########################################################################
            vdc_da_1_d = '\\True Số cách chọn %s bông có đủ hai màu: %s (cách)' %(latex(k_chon), latex(val_d))
            vdc_da_1_s = 'Số cách chọn %s bông có đủ hai màu: 110 (cách)' %(latex(k_chon))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = ('''Để chọn %s bông có đủ hai màu, ta lấy tổng số cách chọn trừ đi các trường hợp chỉ có một màu. \\\\
                             - Trường hợp chỉ có màu hồng: $C_{%s}^{%s} = %s$ cách. \\\\
                             - Trường hợp chỉ có màu trắng: $C_{%s}^{%s} = %s$ cách. \\\\
                             Vậy số cách chọn đủ hai màu là: $%s - %s - %s = %s$ cách.'''
                             %(latex(k_chon), latex(n_hong), latex(k_chon), latex(val_d_all_hong), latex(n_trang), latex(k_chon), latex(val_d_all_trang), latex(val_a), latex(val_d_all_hong), latex(val_d_all_trang), latex(val_d)))

            list_vdc_1 = [vdc_da_1]
            list_vdc_2 = [loigiai_vdc_1]
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Lặp để đảm bảo số đáp án Đúng từ 1 đến 3
            while True:
                ans_nb = random.choice(list_nb_da_1)
                ans_th = random.choice(list_th_da_1)
                ans_vd = random.choice(list_vd_da_1)
                ans_vdc = random.choice(list_vdc_da_1)

                if 1 <= count_true_answers([ans_nb, ans_th, ans_vd, ans_vdc]) <= 3:
                    break

            # Gán kết quả cuối cùng
            shuffled_answers = [ans_nb, ans_th, ans_vd, ans_vdc]
            shuffled_solutions = [loigiai_nb_1, loigiai_th_1, loigiai_vd_1, loigiai_vdc_1]

            # Xuất nội dung theo định dạng ex
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + 
                str(noidungcauhoi) + '\n' +
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

