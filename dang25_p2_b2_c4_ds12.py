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


def bt_dang25_p2_b2_c4_ds12(self):
            # Khai báo biến
            # Khai báo các biến ngẫu nhiên cho bài toán
            # n1: số hộp loại I, n2: số hộp loại II
            n1 = random.randint(3, 5)
            n2 = random.randint(4, 6)
            tong_hop = n1 + n2

            # g1: số sản phẩm tốt hộp I, b1: số phế phẩm hộp I (tổng 100)
            g1 = random.randint(94, 97)
            b1 = 100 - g1

            # g2: số sản phẩm tốt hộp II, b2: số phế phẩm hộp II (tổng 100)
            # Đảm bảo g2 khác g1 để bài toán thú vị hơn
            g2 = random.choice([x for x in range(92, 96) if x != g1])
            b2 = 100 - g2

            # Tính toán các giá trị xác suất bằng Rational để giữ phân số tối giản
            P_B1 = Rational(n1, tong_hop)
            P_B2 = Rational(n2, tong_hop)

            # Xác suất lấy 2 sản phẩm tốt từ hộp 1 và hộp 2
            P_A_B1 = Rational(binomial(g1, 2), binomial(100, 2))
            P_A_B2 = Rational(binomial(g2, 2), binomial(100, 2))

            # Xác suất toàn phần lấy 2 sản phẩm không có phế phẩm (biến cố A)
            P_A = P_B1 * P_A_B1 + P_B2 * P_A_B2

            # Xác suất lấy đúng 1 phế phẩm từ mỗi hộp (biến cố B)
            P_B_cond_B1 = Rational(binomial(g1, 1) * binomial(b1, 1), binomial(100, 2))
            P_B_cond_B2 = Rational(binomial(g2, 1) * binomial(b2, 1), binomial(100, 2))

            # Xác suất toàn phần lấy đúng 1 phế phẩm
            P_B = P_B1 * P_B_cond_B1 + P_B2 * P_B_cond_B2

            # Xác suất hậu nghiệm (Bayes): Biết lấy 1 phế phẩm, tính XS thuộc hộp I
            P_B1_B = (P_B1 * P_B_cond_B1) / P_B

            # Nội dung câu hỏi
            noidungcauhoi = ('''Trong một lô sản phẩm có %s hộp loại I và %s hộp loại II. Biết rằng trong mỗi hộp loại I có %s sản phẩm tốt và %s phế phẩm, trong mỗi hộp loại II có %s sản phẩm tốt và %s phế phẩm. Lấy ngẫu nhiên từ lô sản phẩm đó một hộp, rồi từ hộp đó lấy ra ngẫu nhiên đồng thời hai sản phẩm.''' 
                             % (latex(n1), latex(n2), latex(g1), latex(b1), latex(g2), latex(b2)))

            ########################################################################
            # Câu a) Xác suất chọn hộp loại I
            a_da_d = '\\True Xác suất để hộp được chọn là hộp loại I bằng $%s$' % (latex(P_B1))
            a_da_s = 'Xác suất để hộp được chọn là hộp loại I bằng $%s$' % (latex(Rational(n2, tong_hop)))
            list_a = [a_da_d, a_da_s]
            loigiai_a = 'Số hộp loại I là %s, tổng số hộp là %s. Vậy xác suất chọn hộp loại I là $P(B_1) = \\frac{%s}{%s} = %s$.' % (latex(n1), latex(tong_hop), latex(n1), latex(tong_hop), latex(P_B1))

            ########################################################################
            # Câu b) XS 2 sản phẩm tốt nếu là hộp I
            b_da_d = '\\True Nếu hộp được lấy ra là hộp loại I thì xác suất để cả hai sản phẩm lấy ra không có phế phẩm bằng $%s$' % (latex(P_A_B1))
            b_da_s = 'Nếu hộp được lấy ra là hộp loại I thì xác suất để cả hai sản phẩm lấy ra không có phế phẩm bằng $%s$' % (latex(P_A_B2))
            list_b = [b_da_d, b_da_s]
            loigiai_b = 'Nếu biết là hộp I, ta chọn 2 sản phẩm từ 100 sản phẩm (%s tốt, %s xấu). Xác suất là $P(A|B_1) = \\frac{C_{%s}^2}{C_{100}^2} = %s$.' % (latex(g1), latex(b1), latex(g1), latex(P_A_B1))

            ########################################################################
            # Câu c) XS 2 sản phẩm lấy ra không có phế phẩm (XS toàn phần)
            c_da_d = '\\True Xác suất để cả hai sản phẩm lấy ra không có phế phẩm bằng $%s$' % (latex(P_A))
            c_da_s = 'Xác suất để cả hai sản phẩm lấy ra không có phế phẩm bằng $%s$' % (latex(P_A + Rational(1, 100)))
            list_c = [c_da_d, c_da_s]
            loigiai_c = 'Áp dụng công thức xác suất toàn phần:\\\\ $P(A) = P(B_1).P(A|B_1) + P(B_2).P(A|B_2) = \\frac{%s}{%s} \\cdot \\frac{C_{%s}^2}{C_{100}^2} + \\frac{%s}{%s} \\cdot \\frac{C_{%s}^2}{C_{100}^2} = %s$.' % (latex(n1), latex(tong_hop), latex(g1), latex(n2), latex(tong_hop), latex(g2), latex(P_A))

            ########################################################################
            # Câu d) XS hộp I biết có 1 phế phẩm
            d_da_d = '\\True Biết rằng trong hai sản phẩm lấy ra có đúng một phế phẩm, xác suất để hộp lấy ra là hộp loại I bằng $%s$' % (latex(P_B1_B))
            d_da_s = 'Biết rằng trong hai sản phẩm lấy ra có đúng một phế phẩm, xác suất để hộp lấy ra là hộp loại I bằng $%s$' % (latex(P_B1_B * Rational(1, 2)))
            list_d = [d_da_d, d_da_s]
            loigiai_d = 'Gọi $B$ là biến cố lấy được đúng 1 phế phẩm. Ta có\\\\ $P(B) = P(B_1)P(B|B_1) + P(B_2)P(B|B_2) = \\frac{%s}{%s} \\cdot \\frac{C_{%s}^1 C_{%s}^1}{C_{100}^2} + \\frac{%s}{%s} \\cdot \\frac{C_{%s}^1 C_{%s}^1}{C_{100}^2} = %s$. \\\\ Xác suất cần tìm là $P(B_1|B) = \\frac{P(B_1)P(B|B_1)}{P(B)} = %s$.' % (latex(n1), latex(tong_hop), latex(g1), latex(b1), latex(n2), latex(tong_hop), latex(g2), latex(b2), latex(P_B), latex(P_B1_B))

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Vòng lặp chọn ngẫu nhiên các phương án đúng/sai cho đến khi đạt yêu cầu (1-3 câu đúng)
            while True:
                ans_a = random.choice(list_a)
                ans_b = random.choice(list_b)
                ans_c = random.choice(list_c)
                ans_d = random.choice(list_d)

                current_answers = [ans_a, ans_b, ans_c, ans_d]
                if 1 <= count_true_answers(current_answers) <= 3:
                    break

            # Xuất nội dung theo định dạng yêu cầu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' +
                str(noidungcauhoi) + '\n' +
                '\\choiceTFn \n'
                '{' + str(ans_a) + '}\n'
                '{' + str(ans_b) + '}\n'
                '{' + str(ans_c) + '}\n'
                '{' + str(ans_d) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(loigiai_a) + '\n'
                '\\item ' + str(loigiai_b) + '\n'
                '\\item ' + str(loigiai_c) + '\n'
                '\\item ' + str(loigiai_d) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

