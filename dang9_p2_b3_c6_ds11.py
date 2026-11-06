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


def bt_dang9_p2_b3_c6_ds11(self):
            # Khai báo biến
            # Khai báo biến sympy
            x = symbols('x')

            # --- BƯỚC 1: SINH DỮ LIỆU NGẪU NHIÊN ---
            # Chọn ngẫu nhiên một số chấm mục tiêu cho xúc xắc (1 đến 6)
            target_die = random.randint(1, 6)
            # Chọn ngẫu nhiên loại bài: 0: Bài tây (J, Q, K), 1: Lá Át (A), 2: Lá đỏ (Cơ, Rô)
            card_type_idx = random.choice([0, 1, 2])

            if card_type_idx == 0:
                card_name = "lá bài tây (J, Q, K)"
                n_cards = 12
                card_prob = Rational(12, 52)
            elif card_type_idx == 1:
                card_name = "lá bài Át (A)"
                n_cards = 4
                card_prob = Rational(4, 52)
            else:
                card_name = "lá bài màu đỏ (cơ hoặc rô)"
                n_cards = 26
                card_prob = Rational(26, 52)

            # --- BƯỚC 2: NỘI DUNG CÂU HỎI ---
            noidungcauhoi = "Một người vừa gieo một con xúc xắc cân đối và đồng chất để ghi lại số chấm xuất hiện, sau đó người này tiếp tục chọn ngẫu nhiên một lá bài từ bộ bài 52 lá."

            ########################################################################
            # Nhận biết: Xác suất của xúc xắc
            ########################################################################
            prob_a = Rational(1, 6)
            nb_da_1_d = "\\True Gọi $A$ là biến cố: \"Số chấm của xúc xắc bằng " + str(target_die) + "\", khi đó: $P(A)=\\frac{1}{6}$"
            nb_da_1_s = "Gọi $A$ là biến cố: \"Số chấm của xúc xắc bằng " + str(target_die) + "\", khi đó: $P(A)=\\frac{1}{5}$"
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            loigiai_nb_1 = "Không gian mẫu khi gieo xúc xắc là $\\Omega_1 = \\{1; 2; 3; 4; 5; 6\\} \\Rightarrow n(\\Omega_1) = 6$. Biến cố $A$ có 1 kết quả thuận lợi là $\\{" + str(target_die) + "\\}$. Vậy $P(A) = \\frac{1}{6}$."

            ########################################################################
            # Thông hiểu: Xác suất chọn bài
            ########################################################################
            th_da_1_d = "\\True Gọi $B$ là biến cố: \"Chọn được một " + card_name + "\", khi đó: $P(B)=" + latex(card_prob) + "$"
            th_da_1_s = "Gọi $B$ là biến cố: \"Chọn được một " + card_name + "\", khi đó: $P(B)=\\frac{1}{52}$"
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            loigiai_th_1 = "Số cách chọn 1 lá bài từ 52 lá là $n(\\Omega_2) = 52$. Số " + card_name + " trong bộ bài là " + str(n_cards) + " lá. Vậy $P(B) = \\frac{" + str(n_cards) + "}{52} = " + latex(card_prob) + "$."

            ########################################################################
            # Vận dụng: Xác suất kết hợp (biến cố độc lập)
            ########################################################################
            prob_c = prob_a * card_prob
            vd_da_1_d = "\\True Xác suất để số chấm trên con xúc xắc bằng " + str(target_die) + " và chọn được một " + card_name + " là: $\\frac{" + str(prob_c.p) + "}{" + str(prob_c.q) + "}$"
            vd_da_1_s = "Xác suất để số chấm trên con xúc xắc bằng " + str(target_die) + " và chọn được một " + card_name + " là: $\\frac{1}{156}$"
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            loigiai_vd_1 = "Vì việc gieo xúc xắc và chọn bài là độc lập, nên xác suất cần tìm là $P(A \\cap B) = P(A) \\cdot P(B) = \\frac{1}{6} \\cdot " + latex(card_prob) + " = " + latex(prob_c) + "$."

            ########################################################################
            # Vận dụng cao: Xác suất số chấm trùng số trên bài
            ########################################################################
            # Quy ước: A=1, 2-6 tương ứng. Có 6 giá trị trùng nhau, mỗi giá trị có 4 chất.
            prob_d = Rational(6 * 4, 6 * 52) # = 24/312 = 1/13
            vdc_da_1_d = "\\True Xác suất để số chấm trên con xúc xắc và số của lá bài là giống nhau (với quy ước lá Át là số 1) bằng: $\\frac{1}{13}$"
            vdc_da_1_s = "Xác suất để số chấm trên con xúc xắc và số của lá bài là giống nhau bằng: $\\frac{1}{16}$"
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            loigiai_vdc_1 = "Tổng số kết quả có thể xảy ra là $n(\\Omega) = 6 \\cdot 52 = 312$. Để số chấm và số trên lá bài giống nhau, các cặp có thể là $(1; A), (2; 2), (3; 3), (4; 4), (5; 5), (6; 6)$. Mỗi cặp có 4 trường hợp tương ứng với 4 chất của lá bài. Vậy có $6 \\cdot 4 = 24$ kết quả thuận lợi. Xác suất là $P = \\frac{24}{312} = \\frac{1}{13}$."

            # --- BƯỚC 3: LẶP ĐỂ ĐẢM BẢO SỐ CÂU ĐÚNG TỪ 1 ĐẾN 3 ---
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                nb_sel = random.choice(list_nb_da_1)
                th_sel = random.choice(list_th_da_1)
                vd_sel = random.choice(list_vd_da_1)
                vdc_sel = random.choice(list_vdc_da_1)

                if 1 <= count_true_answers([nb_sel, th_sel, vd_sel, vdc_sel]) <= 3:
                    break

            # --- BƯỚC 4: TỔNG HỢP NỘI DUNG ---
            shuffled_answers = [nb_sel, th_sel, vd_sel, vdc_sel]
            shuffled_solutions = [loigiai_nb_1, loigiai_th_1, loigiai_vd_1, loigiai_vdc_1]

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

