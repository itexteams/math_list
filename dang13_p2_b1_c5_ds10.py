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


def bt_dang13_p2_b1_c5_ds10(self):
            # Khai báo biến
            # n1: Tiếng Anh, n2: Toán, n3: Tiếng Việt
            n1 = random.randint(4, 7)
            n2 = random.randint(8, 12)
            n3 = random.randint(13, 18)

            # Nội dung câu hỏi
            noidungcauhoi = ('''Trên giá sách có %s quyển sách Tiếng Anh khác nhau, %s quyển sách Toán khác nhau và %s quyển sách Tiếng Việt khác nhau.''' 
                             %(latex(n1), latex(n2), latex(n3)))

            ########################################################################
            # Nhận biết (Câu a) ############################################
            ans_a_true_val = n1 + n2 + n3
            ans_a_false_val = n1 + n2
            nb_da_1_d = '\\True Số cách chọn ra một quyển sách từ số sách đã cho: %s (cách)' %(latex(ans_a_true_val))
            nb_da_1_s = 'Số cách chọn ra một quyển sách từ số sách đã cho: %s (cách)' %(latex(ans_a_false_val))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            list_nb_1 = [nb_da_1]
            loigiai_nb_1 = ('''Số cách chọn ra một quyển sách là $%s + %s + %s = %s$ (cách).'''
                            %(latex(n1), latex(n2), latex(n3), latex(ans_a_true_val)))
            list_nb_2 = [loigiai_nb_1]
            combined_nb = list(zip(list_nb_1, list_nb_2))

            ########################################################################
            # Thông hiểu (Câu b) ############################################
            ans_b_true_val = n1 * n2 * n3
            ans_b_false_val = n1 + n2 + n3
            th_da_1_d = '\\True Số cách chọn ba quyển sách khác môn là: %s (cách)' %(latex(ans_b_true_val))
            th_da_1_s = 'Số cách chọn ba quyển sách khác môn là: %s (cách)' %(latex(ans_b_false_val))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            list_th_1 = [th_da_1]
            loigiai_th_1 = ('''Để chọn 3 quyển sách khác môn, ta chọn mỗi môn một quyển. \\\\
                            Số cách chọn là $%s \\cdot %s \\cdot %s = %s$ (cách).'''
                            %(latex(n1), latex(n2), latex(n3), latex(ans_b_true_val)))
            list_th_2 = [loigiai_th_1]
            combined_th = list(zip(list_th_1, list_th_2))

            ########################################################################
            # Vận dụng (Câu c) ############################################
            ans_c_true_val = n1 * n2
            ans_c_false_val = n1 + n2
            vd_da_1_d = '\\True Số cách chọn hai quyển gồm Tiếng Anh và Toán là: %s (cách)' %(latex(ans_c_true_val))
            vd_da_1_s = 'Số cách chọn hai quyển gồm Tiếng Anh và Toán là: %s (cách)' %(latex(ans_c_false_val))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            list_vd_1 = [vd_da_1]
            loigiai_vd_1 = ('''Số cách chọn một quyển Tiếng Anh là %s cách. \\\\
                            Số cách chọn một quyển Toán là %s cách. \\\\
                            Vậy số cách chọn hai quyển gồm Tiếng Anh và Toán là $%s \\cdot %s = %s$ (cách).'''
                            %(latex(n1), latex(n2), latex(n1), latex(n2), latex(ans_c_true_val)))
            list_vd_2 = [loigiai_vd_1]
            combined_vd = list(zip(list_vd_1, list_vd_2))

            ########################################################################
            # Vận dụng cao (Câu d) ############################################
            ans_d_true_val = n1*n2 + n1*n3 + n2*n3
            ans_d_false_val = n1*n2*n3
            vdc_da_1_d = '\\True Số cách chọn hai quyển sách khác môn là: %s (cách)' %(latex(ans_d_true_val))
            vdc_da_1_s = 'Số cách chọn hai quyển sách khác môn là: %s (cách)' %(latex(ans_d_false_val))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            list_vdc_1 = [vdc_da_1]
            loigiai_vdc_1 = ('''Để chọn 2 quyển sách khác môn, ta có các trường hợp sau: \\\\
                             Trường hợp 1: 1 Anh và 1 Toán có $%s \\cdot %s = %s$ (cách). \\\\
                             Trường hợp 2: 1 Anh và 1 Tiếng Việt có $%s \\cdot %s = %s$ (cách). \\\\
                             Trường hợp 3: 1 Toán và 1 Tiếng Việt có $%s \\cdot %s = %s$ (cách). \\\\
                             Tổng số cách chọn là $%s + %s + %s = %s$ (cách).'''
                             %(latex(n1), latex(n2), latex(n1*n2), 
                               latex(n1), latex(n3), latex(n1*n3), 
                               latex(n2), latex(n3), latex(n2*n3),
                               latex(n1*n2), latex(n1*n3), latex(n2*n3), latex(ans_d_true_val)))
            list_vdc_2 = [loigiai_vdc_1]
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Lặp đến khi đáp án có từ 1 đến 3 đúng
            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)

                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                true_count = count_true_answers(answers)

                if 1 <= true_count <= 3:
                    break

            # Gán lại vào list sau khi chọn được bộ đáp án thỏa mãn
            shuffled_answers_nb = [nb_da_1]
            shuffled_solutions_nb = [loigiai_nb_1]
            shuffled_answers_th = [th_da_1]
            shuffled_solutions_th = [loigiai_th_1]
            shuffled_answers_vd = [vd_da_1]
            shuffled_solutions_vd = [loigiai_vd_1]
            shuffled_answers_vdc = [vdc_da_1]
            shuffled_solutions_vdc = [loigiai_vdc_1]

            # Xuất câu hỏi với đáp án và lời giải
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+
                str(noidungcauhoi)+ 
                '\\choiceTFn \n'
                '{'+str(shuffled_answers_nb[0])+'}\n'
                '{'+str(shuffled_answers_th[0])+'}\n'
                '{'+str(shuffled_answers_vd[0])+'}\n'
                '{'+str(shuffled_answers_vdc[0])+'}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(shuffled_solutions_nb[0])+'\n'
                '\\item '+str(shuffled_solutions_th[0])+'\n'
                '\\item '+str(shuffled_solutions_vd[0])+'\n'
                '\\item '+str(shuffled_solutions_vdc[0])+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

