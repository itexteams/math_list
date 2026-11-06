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


def bt_dang5_p2_b1_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # --- KHỞI TẠO DỮ LIỆU NGẪU NHIÊN ---
            # Chọn hệ số k cho quy luật y = kx (mẫu gốc k=2)
            k = random.randint(2, 4)
            # Tập xác định x cố định hoặc có thể random nhẹ
            x_vals = [-5, -3, -1, 0, 1, 2, 5, 8, 9]

            # Tạo tập giá trị y dựa trên y = kx và gây nhiễu 1 vị trí (giống f(5)=8 trong ảnh)
            y_vals = [k * val for val in x_vals]
            idx_err = 6 # Vị trí x=5 trong danh sách x_vals
            y_vals[idx_err] = k * x_vals[idx_err] - random.choice([1, 2])

            # Chuẩn bị chuỗi cho bảng giá trị LaTeX
            str_x = " $&$ ".join(map(str, x_vals))
            str_y = " $&$ ".join(map(str, y_vals))

            # Nội dung câu hỏi
            noidungcauhoi = (r'''Cho hàm số $y = f(x)$ với bảng giá trị tương ứng cho trong bảng sau
            \begin{center}
            \begin{tabular}{|c|c|c|c|c|c|c|c|c|c|}
            \hline
            $x$ & $%s$ \\ \hline
            $y$ & $%s$ \\ \hline
            \end{tabular}
            \end{center}
            Mỗi kết quả dưới đây đúng hay sai?''' % (str_x, str_y))

            ########################################################################
            # Nhận biết ############################################
            set_x_str = "{" + "; ".join(map(str, x_vals)) + "}"
            nb_da_1_d = r'\True Tập xác định là $%s$' % set_x_str
            nb_da_1_s = r'Tập xác định là $\mathbb{R}$'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            # Lời giải Nhận biết
            loigiai_nb_1 = r'Từ giá trị của $x$ trong bảng ta có tập xác định là $%s$.' % set_x_str

            ########################################################################
            # Thông hiểu ############################################
            idx1, idx2 = 4, 1 # x=1 và x=-3
            val_y1, val_y2 = y_vals[idx1], y_vals[idx2]
            tong_dung = val_y1 + val_y2
            tong_sai = 0 # Giống mẫu f(1)+f(-3)=0

            th_da_1_d = r'\True $f(%s) + f(%s) = %s$' % (x_vals[idx1], x_vals[idx2], tong_dung)
            th_da_1_s = r'$f(%s) + f(%s) = %s$' % (x_vals[idx1], x_vals[idx2], tong_sai)
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            # Lời giải Thông hiểu
            loigiai_th_1 = r'$f(%s) + f(%s) = %s + (%s) = %s$.' % (x_vals[idx2], x_vals[idx1], val_y2, val_y1, tong_dung)

            ########################################################################
            # Vận dụng ############################################
            vd_da_1_d = r'\True Hàm số không thể biểu diễn dưới dạng $y = %sx$' % k
            vd_da_1_s = r'$y = %sx$' % k
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            # Lời giải Vận dụng
            loigiai_vd_1 = r'Do $f(%s) = %s$ nên $y \neq %sx$.' % (x_vals[idx_err], y_vals[idx_err], k)

            ########################################################################
            # Vận dụng cao ############################################
            set_y_str = "{" + "; ".join(map(str, y_vals)) + "}"
            vdc_da_1_d = r'\True Tập giá trị là $%s$' % set_y_str
            vdc_da_1_s = r'Tập giá trị là $\mathbb{R}$'
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            # Lời giải Vận dụng cao
            loigiai_vdc_1 = r'Từ giá trị của $y$ trong bảng ta có tập giá trị là $%s$.' % set_y_str

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

            # Gán lại vào list để đúng cấu trúc mẫu truy xuất [0]
            shuffled_answers_nb = [nb_da_1]
            shuffled_solutions_nb = [loigiai_nb_1]

            shuffled_answers_th = [th_da_1]
            shuffled_solutions_th = [loigiai_th_1]

            shuffled_answers_vd = [vd_da_1]
            shuffled_solutions_vd = [loigiai_vd_1]

            shuffled_answers_vdc = [vdc_da_1]
            shuffled_solutions_vdc = [loigiai_vdc_1]

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn theo đúng mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+
            str(noidungcauhoi)+ 
                '\n\\choiceTFn \n'
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

