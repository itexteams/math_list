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


def bt_dang10_p2_b1_c4_ds12(self):
            # Khai báo biến
            # Đảm bảo tổng số người là 900 như đề bài hoặc có thể thay đổi
            total = 900
            m_total = random.randint(45, 55) * 10  # Tổng nam (ví dụ 450-550)
            f_total = total - m_total              # Tổng nữ

            m_e = random.randint(40, m_total // 10 - 2) * 10 # Nam có việc
            m_u = m_total - m_e                              # Nam thất nghiệp

            f_e = random.randint(10, f_total // 10 - 15) * 10 # Nữ có việc
            f_u = f_total - f_e                               # Nữ thất nghiệp

            total_e = m_e + f_e # Tổng người có việc làm
            total_u = m_u + f_u # Tổng người thất nghiệp

            # Tính toán các giá trị xác suất (dạng phân số và số thực)
            prob_m = Rational(m_total, total)
            prob_e = Rational(total_e, total)

            # Tỉ lệ xác suất thất nghiệp của Nữ so với Nam
            p_u_f = Rational(f_u, f_total)
            p_u_m = Rational(m_u, m_total)
            ratio_c = float(p_u_f / p_u_m)
            ratio_str = str(round(ratio_c, 2)).replace('.', ',')

            prob_f_given_e = Rational(f_e, total_e)

            # 2. Nội dung câu hỏi
            noidungcauhoi = ('''Trong một cuộc khảo sát tình trạng công việc trên %s người chỉ có bằng tốt nghiệp THPT tại một địa phương, người ta thu được số liệu như bảng dưới đây:
            \\begin{center}
            \\begin{tabular}{|l|c|c|}
            \\hline
            \\diagbox{Giới tính}{Tình trạng} & Có việc làm & Thất nghiệp \\\\ \\hline
            Nam & %s & %s \\\\ \\hline
            Nữ & %s & %s \\\\ \\hline
            \\end{tabular}
            \\end{center}
            Chọn ngẫu nhiên một người trong nhóm này.''' 
            %(total, m_e, m_u, f_e, f_u))

            ########################################################################
            # Nhận biết (Câu a)
            nb_da_1_d = '\\True Xác suất để chọn được một nam là $%s$' % (latex(prob_m))
            nb_da_1_s = 'Xác suất để chọn được một nam là $%s$' % (latex(Rational(f_total, total)))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = ('''Gọi $A$ là biến cố: "Chọn được một người là nam". \\\\
            Ta có $n(A) = %s$, $n(\\Omega) = %s$. \\\\
            $\\Rightarrow P(A) = \\frac{n(A)}{n(\\Omega)} = \\frac{%s}{%s} = %s$.''' 
            %(m_total, total, m_total, total, latex(prob_m)))

            ########################################################################
            # Thông hiểu (Câu b)
            th_da_1_d = '\\True Xác suất để chọn được một người có việc làm là $%s$' % (latex(prob_e))
            th_da_1_s = 'Xác suất để chọn được một người có việc làm là $%s$' % (latex(Rational(total_u, total)))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = ('''Gọi $B$ là biến cố: "Chọn được một người có việc làm". \\\\
            Ta có $n(B) = %s + %s = %s$, $n(\\Omega) = %s$. \\\\
            $\\Rightarrow P(B) = \\frac{n(B)}{n(\\Omega)} = \\frac{%s}{%s} = %s$.''' 
            %(m_e, f_e, total_e, total, total_e, total, latex(prob_e)))

            ########################################################################
            # Vận dụng (Câu c)
            vd_da_1_d = '\\True Khảo sát cho thấy xác suất để một người thất nghiệp khi người đó là nữ cao gấp %s lần xác suất để một người thất nghiệp khi người đó là nam' % (ratio_str)
            vd_da_1_s = 'Khảo sát cho thấy xác suất để một người thất nghiệp khi người đó là nữ cao gấp %s lần xác suất để một người thất nghiệp khi người đó là nam' % (str(round(ratio_c + 1.5, 1)).replace('.', ','))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = ('''Xác suất một người thất nghiệp khi biết đó là nữ là $P_1 = \\frac{%s}{%s} = %s$. \\\\
            Xác suất một người thất nghiệp khi biết đó là nam là $P_2 = \\frac{%s}{%s} = %s$. \\\\
            Tỉ lệ: $\\frac{P_1}{P_2} = \\frac{%s}{%s} \\approx %s$ lần.''' 
            %(f_u, f_total, latex(p_u_f), m_u, m_total, latex(p_u_m), latex(p_u_f), latex(p_u_m), ratio_str))

            ########################################################################
            # Vận dụng cao (Câu d)
            vdc_da_1_d = '\\True Biết rằng đã chọn được một người có việc làm, xác suất để người này là nữ là $%s$' % (latex(prob_f_given_e))
            vdc_da_1_s = 'Biết rằng đã chọn được một người có việc làm, xác suất để người này là nữ là $%s$' % (latex(Rational(m_e, total_e)))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = ('''Gọi $C$ là biến cố: "Chọn được một người là nữ", $B$ là biến cố: "Chọn được người có việc làm". \\\\
            Ta cần tính xác suất có điều kiện $P(C|B)$. \\\\
            Ta có $P(C|B) = \\frac{n(C \\cap B)}{n(B)} = \\frac{%s}{%s} = %s$.''' 
            %(f_e, total_e, latex(prob_f_given_e)))

            ########################################################################
            # Xử lý chọn đúng/sai (1 đến 3 câu đúng)
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                ans_nb = random.choice(list_nb_da_1)
                ans_th = random.choice(list_th_da_1)
                ans_vd = random.choice(list_vd_da_1)
                ans_vdc = random.choice(list_vdc_da_1)

                if 1 <= count_true_answers([ans_nb, ans_th, ans_vd, ans_vdc]) <= 3:
                    break

            # Xuất nội dung theo định dạng yêu cầu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(ans_nb) + '}\n'
                '{' + str(ans_th) + '}\n'
                '{' + str(ans_vd) + '}\n'
                '{' + str(ans_vdc) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(loigiai_nb_1) + '\n'
                '\\item ' + str(loigiai_th_1) + '\n'
                '\\item ' + str(loigiai_vd_1) + '\n'
                '\\item ' + str(loigiai_vdc_1) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

