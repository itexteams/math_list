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


def bt_dang12_p2_b3_c6_ds11(self):
            # Khai báo biến
            # Khai báo biến và tạo bài toán ngẫu nhiên
            # Số bút xanh (n1) từ 5 đến 7, số bút đỏ (n2) từ 4 đến 5
            n1 = random.randint(5, 7)
            n2 = random.randint(4, 5)
            n_tong = n1 + n2
            k = 3

            # Tính toán các giá trị
            n_omega = binomial(n_tong, k)
            n_A = binomial(n1, k)
            n_B = binomial(n2, k)
            p_A = Rational(n_A, n_omega)
            p_B = Rational(n_B, n_omega)

            # Nội dung câu hỏi
            noidungcauhoi = ('''Một hộp có chứa %s bút mực xanh và %s bút mực đỏ cùng loại, cùng kích thước và khối lượng. Lấy ra ngẫu nhiên đồng thời %s bút từ hộp. Gọi $A$ là biến cố "ba bút lấy ra đều là bút mực xanh", $B$ là biến cố "ba bút lấy ra đều là bút mực đỏ".''' 
                             % (latex(n1), latex(n2), latex(k)))

            ########################################################################
            # Nhận biết - Biến cố A
            # Đúng: n_A, Sai: n_A + một số ngẫu nhiên
            nb_da_1_d = '\\True Có %s kết quả thuận lợi cho biến cố $A$' % (latex(n_A))
            nb_da_1_s = 'Có %s kết quả thuận lợi cho biến cố $A$' % (latex(n_A + random.choice([-5, 5, 10])))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            loigiai_nb_1 = ('''Số kết quả thuận lợi cho biến cố $A$ là $n(A) = C_{%s}^{%s} = %s$.''' 
                            % (latex(n1), latex(k), latex(n_A)))

            ########################################################################
            # Thông hiểu - Biến cố B
            # Đúng: n_B, Sai: n_B + 1
            th_da_1_d = '\\True Có %s kết quả thuận lợi cho biến cố $B$' % (latex(n_B))
            th_da_1_s = 'Có %s kết quả thuận lợi cho biến cố $B$' % (latex(n_B + 1))
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            loigiai_th_1 = ('''Số kết quả thuận lợi cho biến cố $B$ là $n(B) = C_{%s}^{%s} = %s$.''' 
                            % (latex(n2), latex(k), latex(n_B)))

            ########################################################################
            # Vận dụng - Xác suất biến cố A
            vd_da_1_d = '\\True Xác suất của biến cố $A$ bằng $\\frac{%s}{%s}$' % (latex(p_A.p), latex(p_A.q))
            vd_da_1_s = 'Xác suất của biến cố $A$ bằng $\\frac{%s}{%s}$' % (latex(p_A.p + 1), latex(p_A.q))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            loigiai_vd_1 = ('''Số phần tử của không gian mẫu là $n(\\Omega) = C_{%s}^{%s} = %s$. \\\\
            Xác suất của biến cố $A$ là $P(A) = \\frac{n(A)}{n(\\Omega)} = \\frac{%s}{%s} = %s$.''' 
                            % (latex(n_tong), latex(k), latex(n_omega), latex(n_A), latex(n_omega), latex(p_A)))

            ########################################################################
            # Vận dụng cao - Xác suất biến cố B
            vdc_da_1_d = '\\True Xác suất của biến cố $B$ bằng $\\frac{%s}{%s}$' % (latex(p_B.p), latex(p_B.q))
            vdc_da_1_s = 'Xác suất của biến cố $B$ bằng $\\frac{%s}{%s}$' % (latex(p_B.p + 2), latex(p_B.q))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            loigiai_vdc_1 = ('''Xác suất của biến cố $B$ là $P(B) = \\frac{n(B)}{n(\\Omega)} = \\frac{%s}{%s} = %s$.''' 
                             % (latex(n_B), latex(n_omega), latex(p_B)))

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Lặp đến khi có từ 1 đến 3 đáp án đúng
            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)

                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                true_count = count_true_answers(answers)

                if 1 <= true_count <= 3:
                    break

            # Gán lời giải cố định theo thứ tự các ý (a, b, c, d)
            shuffled_solutions = [loigiai_nb_1, loigiai_th_1, loigiai_vd_1, loigiai_vdc_1]

            # Xuất nội dung
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' +
                str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(nb_da_1) + '}\n'
                '{' + str(th_da_1) + '}\n'
                '{' + str(vd_da_1) + '}\n'
                '{' + str(vdc_da_1) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(shuffled_solutions[0]) + '\n'
                '\\item ' + str(shuffled_solutions[1]) + '\n'
                '\\item ' + str(shuffled_solutions[2]) + '\n'
                '\\item ' + str(shuffled_solutions[3]) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

