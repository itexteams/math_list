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


def bt_dang37_p2_b2_c4_ds12(self):
            # Khai báo biến
            # Tổng số nhân viên/vé
            N = 100 
            # Số vé trúng tour du lịch (ngẫu nhiên trong khoảng hợp lý)
            n1 = random.randint(3, 6)   # Thái Lan
            n2 = random.randint(8, 12)  # Đà Nẵng
            n3 = random.randint(15, 25) # Cửa Lò
            # Số vé trúng thưởng 5 triệu đồng
            n4 = N - (n1 + n2 + n3)

            # Các giá trị xác suất tính toán theo Sympy Rational
            prob_A = Rational(n4, N) # P(A)
            prob_B_given_A = Rational(n4 - 1, N - 1) # P(B|A)
            prob_B_given_notA = Rational(n4, N - 1) # P(B|not A)
            prob_B = prob_A # P(B) trong lấy mẫu không hoàn lại luôn bằng P(A)
            prob_A_given_B = Rational(n4 - 1, N - 1) # P(A|B) theo công thức Bayes

            # Nội dung câu hỏi
            noidungcauhoi = ('''Một công ty tổ chức chương trình bốc thăm trúng thưởng nhân dịp nghỉ lễ 30/4 và 1/5 cho %s nhân viên. Trong hộp có %s vé, trong đó có %s vé trúng thưởng tour du lịch miễn phí ở Thái Lan, %s vé trúng thưởng tour du lịch miễn phí ở Đà Nẵng và %s vé trúng thưởng tour du lịch miễn phí tại Cửa Lò (Nghệ An), các vé còn lại trúng thưởng năm triệu đồng. Lần lượt từng nhân viên lên bốc ngẫu nhiên một vé (không hoàn lại).''' 
                             % (latex(N), latex(N), latex(n1), latex(n2), latex(n3)))

            # --- NHẬN BIẾT: Xác suất người thứ nhất ---
            nb_da_1_d = '\\True Xác suất để người bốc thăm thứ nhất bốc được vé trúng thưởng năm triệu đồng là $%s$' % (latex(prob_A))
            nb_da_1_s = 'Xác suất để người bốc thăm thứ nhất bốc được vé trúng thưởng năm triệu đồng là $%s$' % (latex(Rational(n1+n2, N)))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)
            loigiai_nb_1 = ('''Xét biến cố $A$: "Người bốc thăm thứ nhất bốc được vé trúng thưởng năm triệu đồng". \\\\ Ta có số vé trúng thưởng năm triệu đồng là: $%s - (%s + %s + %s) = %s$. \\\\ Xác suất để người bốc thăm thứ nhất bốc được vé trúng thưởng năm triệu đồng là: $P(A) = \\frac{%s}{%s} = %s$.''' 
                            % (latex(N), latex(n1), latex(n2), latex(n3), latex(n4), latex(n4), latex(N), latex(prob_A)))

            # --- THÔNG HIỂU: Xác suất điều kiện P(B|A) ---
            # Tạo đáp án sai bằng cách lấy mẫu có hoàn lại hoặc sai mẫu số
            th_da_1_d = '\\True Xác suất để người bốc thăm thứ hai bốc được vé trúng thưởng năm triệu đồng là $%s$, biết rằng người bốc thăm thứ nhất bốc được vé trúng thưởng năm triệu đồng' % (latex(prob_B_given_A))
            th_da_1_s = 'Xác suất để người bốc thăm thứ hai bốc được vé trúng thưởng năm triệu đồng là $%s$, biết rằng người bốc thăm thứ nhất bốc được vé trúng thưởng năm triệu đồng' % (latex(prob_A))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)
            loigiai_th_1 = ('''Nếu người bốc thăm thứ nhất đã bốc được vé 5 triệu đồng, thì trong hộp còn lại $%s$ vé, trong đó có $%s - 1 = %s$ vé 5 triệu đồng. \\\\ Suy ra $P(B|A) = \\frac{%s}{%s} = %s$.''' 
                            % (latex(N-1), latex(n4), latex(n4-1), latex(n4-1), latex(N-1), latex(prob_B_given_A)))

            # --- VẬN DỤNG: Xác suất toàn phần P(B) ---
            vd_da_1_d = '\\True Xác suất để người bốc thăm thứ hai bốc được vé trúng thưởng năm triệu đồng là $%s$' % (latex(prob_B))
            vd_da_1_s = 'Xác suất để người bốc thăm thứ hai bốc được vé trúng thưởng năm triệu đồng là $%s$' % (latex(Rational(n4-1, N)))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)
            loigiai_vd_1 = ('''Gọi $B$ là biến cố người thứ hai bốc được vé 5 triệu đồng. \\\\ Theo công thức xác suất toàn phần: $P(B) = P(A)P(B|A) + P(\\bar{A})P(B|\\bar{A})$. \\\\ Ta có $P(\\bar{A}) = 1 - P(A) = 1 - %s = %s$. \\\\ Nếu người thứ nhất không bốc được vé 5 triệu, trong hộp còn $%s$ vé 5 triệu trên tổng số $%s$ vé, nên $P(B|\\bar{A}) = \\frac{%s}{%s}$. \\\\ Vậy $P(B) = %s \\cdot %s + %s \\cdot \\frac{%s}{%s} = %s$.''' 
                            % (latex(prob_A), latex(1-prob_A), latex(n4), latex(N-1), latex(n4), latex(N-1), latex(prob_A), latex(prob_B_given_A), latex(1-prob_A), latex(n4), latex(N-1), latex(prob_B)))

            # --- VẬN DỤNG CAO: Công thức Bayes P(A|B) ---
            vdc_da_1_d = '\\True Sau khi người thứ nhất bốc và giữ kín kết quả, biết người thứ hai bốc được vé 5 triệu đồng, thì xác suất người thứ nhất cũng bốc được vé 5 triệu đồng là $%s$' % (latex(prob_A_given_B))
            vdc_da_1_s = 'Sau khi người thứ nhất bốc và giữ kín kết quả, biết người thứ hai bốc được vé 5 triệu đồng, thì xác suất người thứ nhất cũng bốc được vé 5 triệu đồng là $%s$' % (latex(prob_A))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)
            loigiai_vdc_1 = ('''Ta cần tính xác suất có điều kiện $P(A|B)$. \\\\ Theo công thức Bayes, ta có: $P(A|B) = \\frac{P(A)P(B|A)}{P(B)}$. \\\\ Thay các giá trị đã tính: $P(A|B) = \\frac{%s \\cdot %s}{%s} = %s$.''' 
                             % (latex(prob_A), latex(prob_B_given_A), latex(prob_B), latex(prob_A_given_B)))

            # --- Đảm bảo số lượng câu đúng từ 1 đến 3 ---
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                nb_sel = random.choice(list_nb_da_1)
                th_sel = random.choice(list_th_da_1)
                vd_sel = random.choice(list_vd_da_1)
                vdc_sel = random.choice(list_vdc_da_1)
                if 1 <= count_true_answers([nb_sel, th_sel, vd_sel, vdc_sel]) <= 3:
                    break

            # Content format
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(nb_sel) + '}\n'
                '{' + str(th_sel) + '}\n'
                '{' + str(vd_sel) + '}\n'
                '{' + str(vdc_sel) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(loigiai_nb_1) + '\n'
                '\\item ' + str(loigiai_th_1) + '\n'
                '\\item ' + str(loigiai_vd_1) + '\n'
                '\\item ' + str(loigiai_vdc_1) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

