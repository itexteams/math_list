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


def bt_dang11_p2_b3_c5_ds10(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')
            m = random.randint(2, 5)  # Random hằng số m trong (x - m)^4
            n = 4

            # Tính toán các hệ số để dùng cho lời giải và đáp án đúng
            # (x - m)^4 = C(4,0)x^4 - C(4,1)m*x^3 + C(4,2)m^2*x^2 - C(4,3)m^3*x + C(4,4)m^4
            c4 = 1
            c3 = -binomial(4, 1) * m
            c2 = binomial(4, 2) * (m**2)
            c1 = -binomial(4, 3) * (m**3)
            c0 = m**4

            # Tổng các hệ số bậc chẵn: a4 + a2 + a0
            tong_chan = c4 + c2 + c0

            # Nội dung câu hỏi
            noidungcauhoi = ('''Khai triển $\\left( x - %s \\right)^{%s}$.''' 
                             %(latex(m), latex(n)))

            ########################################################################
            # Nhận biết ############################################
            nb_da_1_d = '\\True Hệ số của $x^{4}$ trong khai triển là $%s$' %(latex(c4))
            nb_da_1_s = 'Hệ số của $x^{4}$ trong khai triển là $%s$' %(latex(m))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            list_nb_1 = [nb_da_1]
            loigiai_nb_1 = ('''Hệ số của $x^{4}$ ứng với số hạng $C_{4}^{0} \\cdot x^{4} \\cdot \\left( -%s \\right)^{0} = %s x^{4}$. \\\\ Vậy hệ số là $%s$.''' 
                            %(latex(m), latex(c4), latex(c4)))
            list_nb_2 = [loigiai_nb_1]

            ########################################################################
            # Thông hiểu ############################################
            th_da_1_d = '\\True Hệ số của $x^{3}$ trong khai triển là $%s$' %(latex(c3))
            th_da_1_s = 'Hệ số của $x^{3}$ trong khai triển là $%s$' %(latex(abs(c3)))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            list_th_1 = [th_da_1]
            loigiai_th_1 = ('''Số hạng chứa $x^{3}$ là $C_{4}^{1} \\cdot x^{3} \\cdot \\left( -%s \\right)^{1} = 4 \\cdot \\left( -%s \\right) \\cdot x^{3} = %s x^{3}$. \\\\ Vậy hệ số là $%s$.''' 
                            %(latex(m), latex(m), latex(c3), latex(c3)))
            list_th_2 = [loigiai_th_1]

            ########################################################################
            # Vận dụng ############################################
            vd_da_1_d = '\\True Hệ số của $x^{2}$ trong khai triển là $%s$' %(latex(c2))
            vd_da_1_s = 'Hệ số của $x^{2}$ trong khai triển là $%s$' %(latex(c2 + 10))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            list_vd_1 = [vd_da_1]
            loigiai_vd_1 = ('''Số hạng chứa $x^{2}$ là $C_{4}^{2} \\cdot x^{2} \\cdot \\left( -%s \\right)^{2} = 6 \\cdot %s \\cdot x^{2} = %s x^{2}$. \\\\ Vậy hệ số là $%s$.''' 
                            %(latex(m), latex(m**2), latex(c2), latex(c2)))
            list_vd_2 = [loigiai_vd_1]

            ########################################################################
            # Vận dụng cao ############################################
            vdc_da_1_d = '\\True Tổng các hệ số của các hạng tử có bậc chẵn trong khai triển bằng $%s$' %(latex(tong_chan))
            vdc_da_1_s = 'Tổng các hệ số của các hạng tử có bậc chẵn trong khai triển bằng $%s$' %(latex(tong_chan - 2))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            list_vdc_1 = [vdc_da_1]
            loigiai_vdc_1 = ('''Khai triển đầy đủ: $\\left( x - %s \\right)^{4} = x^{4} %s x^{3} + %s x^{2} %s x + %s$. \\\\ Các hạng tử bậc chẵn là $x^{4}$, $%s x^{2}$ và $%s$. \\\\ Tổng các hệ số bậc chẵn là: $1 + %s + %s = %s$.''' 
                             %(latex(m), latex(c3), latex(c2), latex(c1), latex(c0), latex(c2), latex(c0), latex(c2), latex(c0), latex(tong_chan)))
            list_vdc_2 = [loigiai_vdc_1]

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Lặp đến khi đáp án có từ 1 đến 3 đúng
            while True:
                nb_sel = random.choice(list_nb_da_1)
                th_sel = random.choice(list_th_da_1)
                vd_sel = random.choice(list_vd_da_1)
                vdc_sel = random.choice(list_vdc_da_1)

                answers = [nb_sel, th_sel, vd_sel, vdc_sel]
                true_count = count_true_answers(answers)

                if 1 <= true_count <= 3:
                    # Cập nhật lại các biến được chọn
                    final_nb_ans = nb_sel
                    final_th_ans = th_sel
                    final_vd_ans = vd_sel
                    final_vdc_ans = vdc_sel
                    break

            # Xuất câu hỏi
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+
                str(noidungcauhoi)+ 
                '\n\\choiceTFn \n'
                '{'+str(final_nb_ans)+'}\n'
                '{'+str(final_th_ans)+'}\n'
                '{'+str(final_vd_ans)+'}\n'
                '{'+str(final_vdc_ans)+'}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(loigiai_nb_1)+'\n'
                '\\item '+str(loigiai_th_1)+'\n'
                '\\item '+str(loigiai_vd_1)+'\n'
                '\\item '+str(loigiai_vdc_1)+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

