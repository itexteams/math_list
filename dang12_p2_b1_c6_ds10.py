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


def bt_dang12_p2_b1_c6_ds10(self):
            # Khai báo biến
            # Bước 1: Nghiên cứu đề bài và thiết lập thông số random
            # Random số lượng nam và nữ để bài toán phong phú
            nam = random.randint(6, 7)
            nu = random.randint(5, 6)
            tong = nam + nu
            chon = 4

            # Tính toán các giá trị chuẩn
            # a) Không gian mẫu
            kgm = math.comb(tong, chon)

            # b) Có 2 nam và 2 nữ
            bien_co_b = math.comb(nam, 2) * math.comb(nu, 2)

            # c) Có ít nhất 2 nữ (2 nữ 2 nam + 3 nữ 1 nam + 4 nữ 0 nam)
            bien_co_c = (math.comb(nu, 2) * math.comb(nam, 2) + 
                         math.comb(nu, 3) * math.comb(nam, 1) + 
                         math.comb(nu, 4) * math.comb(nam, 0))

            # d) Có nhiều nhất 2 nữ (0 nữ 4 nam + 1 nữ 3 nam + 2 nữ 2 nam)
            bien_co_d = (math.comb(nu, 0) * math.comb(nam, 4) + 
                         math.comb(nu, 1) * math.comb(nam, 3) + 
                         math.comb(nu, 2) * math.comb(nam, 2))

            # Nội dung câu hỏi
            noidungcauhoi = ('''Một nhóm có %s bạn nam và %s bạn nữ. Chọn ngẫu nhiên cùng một lúc ra %s bạn đi làm công tác tình nguyện.''' 
                             % (latex(nam), latex(nu), latex(chon)))

            ########################################################################
            # Nhận biết - Câu a
            ########################################################################
            sai_a = kgm - random.randint(5, 15)
            nb_da_1_d = '\\True Số phần tử của không gian mẫu là %s' % (latex(kgm))
            nb_da_1_s = 'Số phần tử của không gian mẫu là %s' % (latex(sai_a))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = ('''Số phần tử của không gian mẫu là $n\\left(\\Omega\\right) = C_{%s}^{%s} = %s$.''' 
                            % (latex(tong), latex(chon), latex(kgm)))

            ########################################################################
            # Thông hiểu - Câu b
            ########################################################################
            sai_b = bien_co_b + random.choice([-10, 10, 20])
            th_da_1_d = '\\True Số các kết quả thuận lợi cho biến cố "Trong %s bạn được chọn có 2 bạn nam và 2 bạn nữ" bằng %s' % (latex(chon), latex(bien_co_b))
            th_da_1_s = 'Số các kết quả thuận lợi cho biến cố "Trong %s bạn được chọn có 2 bạn nam và 2 bạn nữ" bằng %s' % (latex(chon), latex(sai_b))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = ('''Chọn 2 bạn nam từ %s bạn nam có $C_{%s}^2$ cách. \\\\
            Chọn 2 bạn nữ từ %s bạn nữ có $C_{%s}^2$ cách. \\\\
            Số kết quả thuận lợi là $C_{%s}^2 \\cdot C_{%s}^2 = %s \\cdot %s = %s$.''' 
                            % (latex(nam), latex(nam), latex(nu), latex(nu), latex(nam), latex(nu), latex(math.comb(nam, 2)), latex(math.comb(nu, 2)), latex(bien_co_b)))

            ########################################################################
            # Vận dụng - Câu c
            ########################################################################
            sai_c = bien_co_c + random.randint(5, 15)
            vd_da_1_d = '\\True Số các kết quả thuận lợi cho biến cố "Trong %s bạn được chọn có ít nhất 2 bạn nữ" bằng %s' % (latex(chon), latex(bien_co_c))
            vd_da_1_s = 'Số các kết quả thuận lợi cho biến cố "Trong %s bạn được chọn có ít nhất 2 bạn nữ" bằng %s' % (latex(chon), latex(sai_c))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = ('''Các trường hợp có ít nhất 2 bạn nữ: \\\\
            - TH1: 2 nữ và 2 nam: $C_{%s}^2 \\cdot C_{%s}^2 = %s$. \\\\
            - TH2: 3 nữ và 1 nam: $C_{%s}^3 \\cdot C_{%s}^1 = %s$. \\\\
            - TH3: 4 nữ và 0 nam: $C_{%s}^4 \\cdot C_{%s}^0 = %s$. \\\\
            Tổng số kết quả thuận lợi là $%s + %s + %s = %s$.''' 
                            % (latex(nu), latex(nam), latex(math.comb(nu, 2) * math.comb(nam, 2)),
                               latex(nu), latex(nam), latex(math.comb(nu, 3) * math.comb(nam, 1)),
                               latex(nu), latex(nam), latex(math.comb(nu, 4) * math.comb(nam, 0)),
                               latex(math.comb(nu, 2) * math.comb(nam, 2)),
                               latex(math.comb(nu, 3) * math.comb(nam, 1)),
                               latex(math.comb(nu, 4) * math.comb(nam, 0)),
                               latex(bien_co_c)))

            ########################################################################
            # Vận dụng cao - Câu d
            ########################################################################
            sai_d = bien_co_d - random.randint(5, 10)
            vdc_da_1_d = '\\True Số các kết quả thuận lợi cho biến cố "Trong %s bạn được chọn có nhiều nhất 2 bạn nữ" bằng %s' % (latex(chon), latex(bien_co_d))
            vdc_da_1_s = 'Số các kết quả thuận lợi cho biến cố "Trong %s bạn được chọn có nhiều nhất 2 bạn nữ" bằng %s' % (latex(chon), latex(sai_d))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = ('''Các trường hợp có nhiều nhất 2 bạn nữ: \\\\
            - TH1: 0 nữ và 4 nam: $C_{%s}^0 \\cdot C_{%s}^4 = %s$. \\\\
            - TH2: 1 nữ và 3 nam: $C_{%s}^1 \\cdot C_{%s}^3 = %s$. \\\\
            - TH3: 2 nữ và 2 nam: $C_{%s}^2 \\cdot C_{%s}^2 = %s$. \\\\
            Tổng số kết quả thuận lợi là $%s + %s + %s = %s$.''' 
                             % (latex(nu), latex(nam), latex(math.comb(nu, 0) * math.comb(nam, 4)),
                                latex(nu), latex(nam), latex(math.comb(nu, 1) * math.comb(nam, 3)),
                                latex(nu), latex(nam), latex(math.comb(nu, 2) * math.comb(nam, 2)),
                                latex(math.comb(nu, 0) * math.comb(nam, 4)),
                                latex(math.comb(nu, 1) * math.comb(nam, 3)),
                                latex(math.comb(nu, 2) * math.comb(nam, 2)),
                                latex(bien_co_d)))

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Vòng lặp đảm bảo có từ 1 đến 3 đáp án đúng
            while True:
                ans_a = random.choice(list_nb_da_1)
                ans_b = random.choice(list_th_da_1)
                ans_c = random.choice(list_vd_da_1)
                ans_d = random.choice(list_vdc_da_1)

                current_answers = [ans_a, ans_b, ans_c, ans_d]
                if 1 <= count_true_answers(current_answers) <= 3:
                    break

            # Gán lại giá trị đã chọn
            shuffled_answers = [ans_a, ans_b, ans_c, ans_d]
            shuffled_solutions = [loigiai_nb_1, loigiai_th_1, loigiai_vd_1, loigiai_vdc_1]

            # Xuất nội dung theo định dạng yêu cầu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + 
                str(noidungcauhoi) + '\n'
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

