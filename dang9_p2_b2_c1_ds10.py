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


def bt_dang9_p2_b2_c1_ds10(self):
            # Khai báo biến
            # 2. nA + nB - nAB <= nTotal (tổng số người khảo sát)

            nTotal = random.randint(100, 200)
            nA = random.randint(40, 70)
            nB = random.randint(45, 75)
            # Đảm bảo nAB nhỏ hơn nA và nB
            nAB = random.randint(20, min(nA, nB) - 5)

            # Các giá trị tính toán
            nUnion = nA + nB - nAB
            nNeither = nTotal - nUnion

            # Nội dung câu hỏi
            noidungcauhoi = (f"Trong một cuộc khảo sát người tiêu dùng, trong {nTotal} người uống cà phê được khảo sát, "
                             f"có {nA} người thêm đường, {nB} người thêm sữa và {nAB} người thêm cả đường và sữa. "
                             f"Trong số {nTotal} người đó, gọi $A$ là tập hợp những người uống cà phê có thêm đường và "
                             f"$B$ là tập hợp những người uống cà phê có thêm sữa.")

            ######################################################################## Nhận biết ############################################
            # Kiểm tra khái niệm tập hợp
            nb_da_1_d = r'\True $A \cap B$ là tập hợp những người uống cà phê có thêm cả đường và sữa'
            nb_da_1_s = r'$A \cup B$ là tập hợp những người uống cà phê có thêm cả đường và sữa'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            loigiai_nb_1 = (r"Kí hiệu $U$ là tập hợp người được khảo sát. Khi đó tập $A \cap B$ là tập hợp người thêm cả đường và sữa "
                            r"và $A \cup B$ là tập hợp người thêm ít nhất đường hoặc sữa.")

            ######################################################################## Thông hiểu ############################################
            # Kiểm tra việc đọc dữ liệu
            th_da_1_d = f'\\True $n(A)={nA}; n(B)={nB}; n(A \\cap B)={nAB}$'
            th_da_1_s = f'$n(A)={nB}; n(B)={nA}; n(A \\cap B)={nAB}$'
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            loigiai_th_1 = f"Theo giả thiết ta có $n(A)={nA}; n(B)={nB}; n(A \\cap B)={nAB}$."

            ######################################################################## Vận dụng ############################################
            # Tính số người thêm ít nhất một thứ (Hợp)
            sai_union = nA + nB # Lỗi sai thường gặp là quên trừ phần giao
            vd_da_1_d = f'\\True Số người uống cà phê thêm ít nhất đường hoặc sữa là {nUnion}'
            vd_da_1_s = f'Số người uống cà phê thêm ít nhất đường hoặc sữa là {sai_union}'
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            loigiai_vd_1 = (f"Số người thêm ít nhất đường hoặc sữa là "
                            f"$n(A \\cup B) = n(A) + n(B) - n(A \\cap B) = {nA} + {nB} - {nAB} = {nUnion}$.")

            ######################################################################## Vận dụng cao ############################################
            # Tính số người không thêm gì cả
            vdc_da_1_d = f'\\True Số người uống cà phê không thêm cả đường và sữa là {nNeither}'
            vdc_da_1_s = f'Số người uống cà phê không thêm cả đường và sữa là {nTotal - nA}'
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            loigiai_vdc_1 = (f"Số người không thêm cả đường và sữa là $n(U) - n(A \\cup B) = {nTotal} - {nUnion} = {nNeither}$.")

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

            # Gán vào list để shuffle (theo mẫu của bạn)
            shuffled_answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
            shuffled_solutions = [loigiai_nb_1, loigiai_th_1, loigiai_vd_1, loigiai_vdc_1]

            # Xuất nội dung
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + 
                str(noidungcauhoi) + '\n' +
                '\\choiceTFn \n'
                '{'+str(shuffled_answers[0])+'}\n'
                '{'+str(shuffled_answers[1])+'}\n'
                '{'+str(shuffled_answers[2])+'}\n'
                '{'+str(shuffled_answers[3])+'}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(shuffled_solutions[0])+'\n'
                '\\item '+str(shuffled_solutions[1])+'\n'
                '\\item '+str(shuffled_solutions[2])+'\n'
                '\\item '+str(shuffled_solutions[3])+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n'
                '\\end{minipage}\n\n')
            return content

