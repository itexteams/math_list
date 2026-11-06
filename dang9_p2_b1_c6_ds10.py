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


def bt_dang9_p2_b1_c6_ds10(self):
            # Khai báo biến
            # Hàm kiểm tra số nguyên tố để tính toán đáp án (d)
            def is_prime(n):
                if n < 2:
                    return False
                for i in range(2, int(math.sqrt(n)) + 1):
                    if n % i == 0:
                        return False
                return True

            # --- BƯỚC 1: NGẪU NHIÊN HÓA THÔNG SỐ ---
            # Giả sử M là số tự nhiên từ 18 đến 25 (trong hình là 20)
            M = randint(18, 25)

            # Tập hợp A = {10, 11, ..., M-1}
            A = list(range(10, M))
            n_omega_correct = len(A)

            # Biến cố B: Lấy được số lẻ
            B_list = [x for x in A if x % 2 != 0]
            n_B_correct = len(B_list)

            # Biến cố C: Lấy được số chia hết cho 3
            C_list = [x for x in A if x % 3 == 0]
            n_C_correct = len(C_list)

            # Biến cố D: Lấy được số nguyên tố
            D_list = [x for x in A if is_prime(x)]
            n_D_correct = len(D_list)

            # --- NỘI DUNG CÂU HỎI ---
            noidungcauhoi = ('''Gọi $A$ là tập hợp các số tự nhiên có $2$ chữ số nhỏ hơn $%s$. Lấy ra $1$ số tự nhiên bất kỳ trong $A$.''' 
                             %(M))

            ########################################################################
            # Nhận biết (Câu a - n(Omega)) ############################################
            nb_da_1_d = '\\True $n(\\Omega) = %s$' % (n_omega_correct)
            nb_da_1_s = '$n(\\Omega) = %s$' % (n_omega_correct + randint(1, 3))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = ('''Tập hợp các số tự nhiên có $2$ chữ số nhỏ hơn $%s$ là $A = \\{%s; %s; \\dots; %s\\}$.\\\\ 
                            Số phần tử của không gian mẫu là $n(\\Omega) = %s - 10 = %s$.'''
                            % (M, A[0], A[1], A[-1], M, n_omega_correct))

            list_nb_1 = [nb_da_1]
            list_nb_2 = [loigiai_nb_1]

            ########################################################################
            # Thông hiểu (Câu b - n(B) số lẻ) ############################################
            th_da_1_d = '\\True Gọi $B$ là biến cố: "Lấy được một số tự nhiên lẻ". Khi đó: $n(B) = %s$' % (n_B_correct)
            th_da_1_s = 'Gọi $B$ là biến cố: "Lấy được một số tự nhiên lẻ". Khi đó: $n(B) = %s$' % (n_B_correct + 1)
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = ('''Các số lẻ trong tập hợp $A$ là: $%s$.\\\\ 
                            Vậy số phần tử của biến cố $B$ là $n(B) = %s$.'''
                            % ("; ".join(map(str, B_list)), n_B_correct))

            list_th_1 = [th_da_1]
            list_th_2 = [loigiai_th_1]

            ########################################################################
            # Vận dụng (Câu c - n(C) chia hết cho 3) ####################################
            vd_da_1_d = '\\True Gọi $C$ là biến cố: "Lấy được một số tự nhiên chia hết cho $3$". Khi đó: $n(C) = %s$' % (n_C_correct)
            vd_da_1_s = 'Gọi $C$ là biến cố: "Lấy được một số tự nhiên chia hết cho $3$". Khi đó: $n(C) = %s$' % (max(1, n_C_correct - 1))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = ('''Các số trong tập hợp $A$ chia hết cho $3$ là: $%s$.\\\\ 
                            Vậy số phần tử của biến cố $C$ là $n(C) = %s$.'''
                            % ("; ".join(map(str, C_list)), n_C_correct))

            list_vd_1 = [vd_da_1]
            list_vd_2 = [loigiai_vd_1]

            ########################################################################
            # Vận dụng cao (Câu d - n(D) số nguyên tố) #################################
            vdc_da_1_d = '\\True Gọi $D$ là biến cố: "Lấy được một số nguyên tố". Khi đó: $n(D) = %s$' % (n_D_correct)
            vdc_da_1_s = 'Gọi $D$ là biến cố: "Lấy được một số nguyên tố". Khi đó: $n(D) = %s$' % (n_D_correct - 1 if n_D_correct > 2 else n_D_correct + 2)
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = ('''Các số nguyên tố trong tập hợp $A$ là: $%s$.\\\\ 
                            Vậy số phần tử của biến cố $D$ là $n(D) = %s$.'''
                            % ("; ".join(map(str, D_list)), n_D_correct))

            list_vdc_1 = [vdc_da_1]
            list_vdc_2 = [loigiai_vdc_1]

            # --- VÒNG LẶP ĐẢM BẢO SỐ CÂU ĐÚNG TỪ 1 ĐẾN 3 ---
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                nb_sel = random.choice(list_nb_da_1)
                th_sel = random.choice(list_th_da_1)
                vd_sel = random.choice(list_vd_da_1)
                vdc_sel = random.choice(list_vdc_da_1)

                answers = [nb_sel, th_sel, vd_sel, vdc_sel]
                true_count = count_true_answers(answers)

                if 1 <= true_count <= 3:
                    break

            # Gán kết quả cuối cùng
            shuffled_answers_nb = [nb_sel]
            shuffled_answers_th = [th_sel]
            shuffled_answers_vd = [vd_sel]
            shuffled_answers_vdc = [vdc_sel]

            # Xuất nội dung theo định dạng yêu cầu
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
                '\\item '+str(list_nb_2[0])+'\n'
                '\\item '+str(list_th_2[0])+'\n'
                '\\item '+str(list_vd_2[0])+'\n'
                '\\item '+str(list_vdc_2[0])+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

