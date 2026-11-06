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


def bt_dang17_p2_b1_c4_ds12(self):
            # Khai báo biến
            # P(A): Vòng sơ khảo, P(B|A): Vòng bán kết, P(C|B): Vòng chung kết
            p1 = 0.5  # 50%
            p2 = 0.3  # 30%
            p3 = 0.2  # 20%

            # Tính toán các giá trị xác suất
            p_a = p1
            p_b = round(p1 * p2, 4)
            p_c = round(p1 * p2 * p3, 4)

            # Tính toán cho câu d
            p_c_ngang_a = round(1 - (p_c / p_a), 4)
            p_c_ngang = round(1 - p_c, 4)
            p_a_given_c_ngang = round((p_c_ngang_a * p_a) / p_c_ngang, 4)
            threshold = 0.49

            # Định dạng số thập phân dùng dấu phẩy cho hiển thị
            def format_dec(val):
                return str(val).replace('.', ',')

            # Nội dung câu hỏi
            noidungcauhoi = ('''Các thí sinh tham dự một cuộc thi hoa khôi phải trải qua ba vòng thi: Vòng sơ khảo, Vòng bán kết và Vòng chung kết. Biết rằng, ban tổ chức sẽ chọn ra %s\\%% thí sinh đã đăng kí để vào Vòng sơ khảo. Khi kết thúc vòng sơ khảo, ban tổ chức sẽ chọn ra %s\\%% thí sinh của Vòng sơ khảo để vào Vòng bán kết. Khi kết thúc vòng bán kết, ban tổ chức sẽ chọn ra %s\\%% thí sinh của Vòng bán kết để vào Vòng chung kết. Chọn ngẫu nhiên 1 thí sinh đăng kí tham dự cuộc thi hoa khôi.''' 
                             % (int(p1*100), int(p2*100), int(p3*100)))

            ########################################################################
            # Nhận biết ############################################
            nb_da_1_d = '\\True Xác suất để thí sinh được chọn lọt vào Vòng sơ khảo là %s' % format_dec(p_a)
            nb_da_1_s = 'Xác suất để thí sinh được chọn lọt vào Vòng sơ khảo là %s' % format_dec(p_b)
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = ('''Gọi $A, B, C$ lần lượt là biến cố thí sinh được chọn lọt vào Vòng sơ khảo, Vòng bán kết và Vòng chung kết. \\\\ Có %s\\%% thí sinh lọt vào vòng sơ khảo nên $P(A)=%s$.''' 
                            % (int(p1*100), format_dec(p_a)))

            list_nb_2 = [loigiai_nb_1]
            combined_nb = list(zip([nb_da_1], list_nb_2))

            ########################################################################
            # Thông hiểu ############################################
            th_da_1_d = '\\True Xác suất để thí sinh được chọn lọt vào Vòng bán kết là %s' % format_dec(p_b)
            th_da_1_s = 'Xác suất để thí sinh được chọn lọt vào Vòng bán kết là %s' % format_dec(p2)
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = ('''Xác suất để thí sinh lọt vào Vòng bán kết là: \\\\ $P(B)=P(AB)=P(B|A)P(A)=%s \\cdot %s = %s$.''' 
                            % (format_dec(p2), format_dec(p_a), format_dec(p_b)))

            list_th_2 = [loigiai_th_1]
            combined_th = list(zip([th_da_1], list_th_2))

            ########################################################################
            # Vận dụng ############################################
            vd_da_1_d = '\\True Xác suất thí sinh được chọn lọt vào Vòng chung kết là %s' % format_dec(p_c)
            vd_da_1_s = 'Xác suất thí sinh được chọn lọt vào Vòng chung kết là %s' % format_dec(0.05)
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = ('''Xác suất để thí sinh lọt vào Vòng chung kết là: \\\\ $P(C)=P(ABC)=P(C|AB)P(AB)=%s \\cdot %s = %s$.''' 
                            % (format_dec(p3), format_dec(p_b), format_dec(p_c)))

            list_vd_2 = [loigiai_vd_1]
            combined_vd = list(zip([vd_da_1], list_vd_2))

            ########################################################################
            # Vận dụng cao ############################################
            vdc_da_1_d = '\\True Biết rằng thí sinh được chọn không lọt vào Vòng chung kết, xác suất thí sinh đó lọt vào Vòng sơ khảo nhỏ hơn %s' % format_dec(threshold)
            vdc_da_1_s = 'Biết rằng thí sinh được chọn không lọt vào Vòng chung kết, xác suất thí sinh đó lọt vào Vòng sơ khảo lớn hơn %s' % format_dec(threshold)
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = ('''Ta có: \\\\ $P(\\bar{C}|A)=1-P(C|A)=1-\\frac{P(C)}{P(A)}=1-\\frac{%s}{%s}=%s$. \\\\ $P(A|\\bar{C})=\\frac{P(\\bar{C}|A)P(A)}{P(\\bar{C})}=\\frac{%s \\cdot %s}{1-%s}=\\frac{47}{97} \\approx 0,485 < %s$.''' 
                             % (format_dec(p_c), format_dec(p_a), format_dec(p_c_ngang_a), format_dec(p_c_ngang_a), format_dec(p_a), format_dec(p_c), format_dec(threshold)))

            list_vdc_2 = [loigiai_vdc_1]
            combined_vdc = list(zip([vdc_da_1], list_vdc_2))

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Vòng lặp kiểm soát số lượng câu đúng từ 1 đến 3
            while True:
                d1 = random.choice(list_nb_da_1)
                d2 = random.choice(list_th_da_1)
                d3 = random.choice(list_vd_da_1)
                d4 = random.choice(list_vdc_da_1)

                if 1 <= count_true_answers([d1, d2, d3, d4]) <= 3:
                    break

            # Xuất nội dung
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + 
                str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + d1 + '}\n'
                '{' + d2 + '}\n'
                '{' + d3 + '}\n'
                '{' + d4 + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + loigiai_nb_1 + '\n'
                '\\item ' + loigiai_th_1 + '\n'
                '\\item ' + loigiai_vd_1 + '\n'
                '\\item ' + loigiai_vdc_1 + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

