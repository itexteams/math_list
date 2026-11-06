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


def bt_dang3_p2_b1_c6_ds11(self):
            # Khai báo biến
            # Nội dung câu hỏi gốc
            noidungcauhoi = ('''Cho $A$ và $B$ là hai biến cố liên quan cùng một phép thử $T$.''')

            ########################################################################
            # Nhận biết - Công thức cộng xác suất cho biến cố xung khắc
            ########################################################################
            nb_da_1_d = '\\True Nếu $A$ và $B$ là hai biến cố xung khắc thì $P\\left( A \\cup B \\right) = P\\left( A \\right) + P\\left( B \\right)$'
            nb_da_1_s = 'Nếu $A$ và $B$ là hai biến cố xung khắc thì $P\\left( A \\cup B \\right) = P\\left( A \\right) \\cdot P\\left( B \\right)$'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = ('''Theo quy tắc cộng xác suất: Nếu hai biến cố $A$ và $B$ xung khắc ($A \\cap B = \\emptyset$) thì xác suất của biến cố hợp bằng tổng các xác suất của mỗi biến cố. Do đó khẳng định $P\\left( A \\cup B \\right) = P\\left( A \\right) + P\\left( B \\right)$ là đúng.''')

            list_nb_1 = [nb_da_1]
            list_nb_2 = [loigiai_nb_1]
            combined_nb = list(zip(list_nb_1, list_nb_2))

            ########################################################################
            # Thông hiểu - Công thức nhân xác suất cho biến cố độc lập
            ########################################################################
            th_da_1_d = '\\True Nếu $A$ và $B$ là hai biến cố độc lập thì $P\\left( AB \\right) = P\\left( A \\right) \\cdot P\\left( B \\right)$'
            th_da_1_s = 'Nếu $A$ và $B$ là hai biến cố độc lập thì $P\\left( AB \\right) = P\\left( A \\right) + P\\left( B \\right)$'
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = ('''Theo quy tắc nhân xác suất: Hai biến cố $A$ và $B$ được gọi là độc lập nếu việc xảy ra hay không xảy ra của biến cố này không làm thay đổi xác suất xảy ra của biến cố kia. Khi đó $P\\left( A \\cap B \\right) = P\\left( A \\right) \\cdot P\\left( B \\right)$.''')

            list_th_1 = [th_da_1]
            list_th_2 = [loigiai_th_1]
            combined_th = list(zip(list_th_1, list_th_2))

            ########################################################################
            # Vận dụng - Mối quan hệ giữa xung khắc và đối nhau (Chiều sai)
            ########################################################################
            vd_da_1_d = '\\True Hai biến cố xung khắc chưa chắc là hai biến cố đối'
            vd_da_1_s = 'Hai biến cố xung khắc là hai biến cố đối'
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = ('''Hai biến cố xung khắc là hai biến cố không cùng xảy ra ($A \\cap B = \\emptyset$). Hai biến cố đối là hai biến cố xung khắc và có tổng hợp bằng không gian mẫu ($A \\cup B = \\Omega$). Vì vậy, xung khắc là điều kiện cần nhưng chưa đủ để đối nhau. Ví dụ: gieo con xúc sắc, biến cố "xuất hiện mặt 1 chấm" và "xuất hiện mặt 2 chấm" là xung khắc nhưng không phải là hai biến cố đối.''')

            list_vd_1 = [vd_da_1]
            list_vd_2 = [loigiai_vd_1]
            combined_vd = list(zip(list_vd_1, list_vd_2))

            ########################################################################
            # Vận dụng cao - Mối quan hệ giữa đối nhau và xung khắc (Chiều đúng)
            ########################################################################
            vdc_da_1_d = '\\True Hai biến cố đối là hai biến cố xung khắc'
            vdc_da_1_s = 'Hai biến cố đối không phải là hai biến cố xung khắc'
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = ('''Theo định nghĩa, hai biến cố đối nhau $A$ và $\\overline{A}$ thì chúng không bao giờ cùng xảy ra trong một phép thử, tức là $A \\cap \\overline{A} = \\emptyset$. Theo định nghĩa biến cố xung khắc, điều này khẳng định rằng hai biến cố đối luôn luôn là hai biến cố xung khắc.''')

            list_vdc_1 = [vdc_da_1]
            list_vdc_2 = [loigiai_vdc_1]
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Lặp đến khi đáp án có từ 1 đến 3 câu đúng để đảm bảo tính khách quan của đề thi
            while True:
                nb_sel = random.choice(list_nb_da_1)
                th_sel = random.choice(list_th_da_1)
                vd_sel = random.choice(list_vd_da_1)
                vdc_sel = random.choice(list_vdc_da_1)

                answers_check = [nb_sel, th_sel, vd_sel, vdc_sel]
                true_count = count_true_answers(answers_check)

                if 1 <= true_count <= 3:
                    # Gán lại giá trị được chọn vào các biến sử dụng trong content
                    nb_da_1 = nb_sel
                    th_da_1 = th_sel
                    vd_da_1 = vd_sel
                    vdc_da_1 = vdc_sel
                    break

            # Cập nhật lại danh sách kết hợp sau khi đã chốt đáp án ngẫu nhiên
            combined_nb = list(zip([nb_da_1], list_nb_2))
            combined_th = list(zip([th_da_1], list_th_2))
            combined_vd = list(zip([vd_da_1], list_vd_2))
            combined_vdc = list(zip([vdc_da_1], list_vdc_2))

            # Tách lại danh sách
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            # Xuất câu hỏi theo định dạng LaTeX yêu cầu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' +
                str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(shuffled_answers_nb[0]) + '}\n'
                '{' + str(shuffled_answers_th[0]) + '}\n'
                '{' + str(shuffled_answers_vd[0]) + '}\n'
                '{' + str(shuffled_answers_vdc[0]) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(shuffled_solutions_nb[0]) + '\n'
                '\\item ' + str(shuffled_solutions_th[0]) + '\n'
                '\\item ' + str(shuffled_solutions_vd[0]) + '\n'
                '\\item ' + str(shuffled_solutions_vdc[0]) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

