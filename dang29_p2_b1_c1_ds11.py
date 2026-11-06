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


def bt_dang29_p2_b1_c1_ds11(self):
            # Khai báo biến
            # Để tạo ra nhiều câu hỏi khác nhau, ta random các hệ số nguyên và phân số để tính hiệu số giữa hai góc
            k_a = random.choice([1, 3, 5]) # Chọn số lẻ, hiệu (k_a + 2)*pi - k_a*pi = 2pi -> Luôn Đúng
            k_b = random.choice([2, 4, 6]) # Chọn số chẵn, hiệu (k_b + 1)*pi - k_b*pi = pi -> Luôn Sai

            # Đối với phân số góc phần tư: chọn ngẫu nhiên mẫu số mẫu_c (3, 4, 6)
            mau_c = random.choice([3, 4, 6])
            tu_c1 = -1
            tu_c2 = 2 * mau_c - 1 # Hiệu: (2*mau_c - 1)/mau_c - (-1/mau_c) = 2 -> Hiệu là 2pi -> Luôn Đúng
            tu_c3 = 3 * mau_c - 1 # Hiệu: (3*mau_c - 1)/mau_c - (-1/mau_c) = 3 -> Hiệu là 3pi -> Luôn Sai

            # Nội dung câu hỏi theo cấu trúc mẫu dùng định dạng %s
            noidungcauhoi = ('''Các khẳng định sau đúng hay sai?''')

            ########################################################################
            # Nhận biết ############################################
            # Câu a (Mẫu gốc: Đúng)
            nb_da_1_d = '\\True Cặp góc lượng giác $%s\\pi$ và $%s\\pi$ có cùng điểm biểu diễn trên đường tròn lượng giác' %(latex(k_a), latex(k_a + 2))
            nb_da_1_s = 'Cặp góc lượng giác $%s\\pi$ và $%s\\pi$ không có cùng điểm biểu diễn trên đường tròn lượng giác' %(latex(k_a), latex(k_a + 2))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            list_nb_1 = [nb_da_1]

            loigiai_nb_1 = ('''Ta có hiệu số đo giữa hai góc lượng giác là: $%s\\pi - %s\\pi = 2\\pi$.\\\\
            Vì hiệu số đo của hai góc bằng một bội nguyên lần của $2\\pi$ ($2\\pi = 1 \\cdot 2\\pi$) nên hai góc lượng giác này có cùng điểm biểu diễn trên đường tròn lượng giác.''' %(latex(k_a + 2), latex(k_a)))
            list_nb_2 = [loigiai_nb_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu ############################################
            # Câu b (Mẫu gốc: Sai)
            th_da_1_s = 'Cặp góc lượng giác $%s\\pi$ và $%s\\pi$ có cùng điểm biểu diễn trên đường tròn lượng giác' %(latex(k_b), latex(k_b + 1))
            th_da_1_d = '\\True Cặp góc lượng giác $%s\\pi$ và $%s\\pi$ có điểm biểu diễn đối xứng nhau qua gốc tọa độ trên đường tròn lượng giác' %(latex(k_b), latex(k_b + 1))
            list_th_da_1 = [th_da_1_s, th_da_1_d]
            th_da_1 = random.choice(list_th_da_1)

            list_th_1 = [th_da_1]

            loigiai_th_1 = ('''Ta có hiệu số đo giữa hai góc lượng giác là: $%s\\pi - %s\\pi = \\pi$.\\\\
            Vì hiệu số đo không phải là một bội nguyên của $2\\pi$ nên hai góc lượng giác này không có cùng điểm biểu diễn trên đường tròn lượng giác.''' %(latex(k_b + 1), latex(k_b)))
            list_th_2 = [loigiai_th_1]

            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## 
            # Vận dụng ############################################
            # Câu c (Mẫu gốc: Đúng)
            vd_da_1_d = '\\True Cặp góc lượng giác $-\\frac{\\pi}{%s}$ và $\\frac{%s\\pi}{%s}$ có cùng điểm biểu diễn trên đường tròn lượng giác' %(latex(mau_c), latex(tu_c2), latex(mau_c))
            vd_da_1_s = 'Cặp góc lượng giác $-\\frac{\\pi}{%s}$ và $\\frac{%s\\pi}{%s}$ không có cùng điểm biểu diễn trên đường tròn lượng giác' %(latex(mau_c), latex(tu_c2), latex(mau_c))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            list_vd_1 = [vd_da_1]

            loigiai_vd_1 = ('''Ta có hiệu số đo giữa hai góc lượng giác là:\\\\
            $\\frac{%s\\pi}{%s} - \\left(-\\frac{\\pi}{%s}\\right) = \\frac{%s\\pi}{%s} = 2\\pi$.\\\\
            Hiệu số đo bằng $2\\pi$ nên cặp góc lượng giác này có cùng điểm biểu diễn trên đường tròn lượng giác.''' %(latex(tu_c2), latex(mau_c), latex(mau_c), latex(tu_c2 + 1), latex(mau_c)))
            list_vd_2 = [loigiai_vd_1]

            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## 
            # Vận dụng cao ############################################
            # Câu d (Mẫu gốc: Sai)
            vdc_da_1_s = 'Cặp góc lượng giác $-\\frac{\\pi}{%s}$ và $\\frac{%s\\pi}{%s}$ có cùng điểm biểu diễn trên đường tròn lượng giác' %(latex(mau_c), latex(tu_c3), latex(mau_c))
            vdc_da_1_d = '\\True Cặp góc lượng giác $-\\frac{\\pi}{%s}$ và $\\frac{%s\\pi}{%s}$ không có cùng điểm biểu diễn trên đường tròn lượng giác' %(latex(mau_c), latex(tu_c3), latex(mau_c))
            list_vdc_da_1 = [vdc_da_1_s, vdc_da_1_d]
            vdc_da_1 = random.choice(list_vdc_da_1)

            list_vdc_1 = [vdc_da_1]

            loigiai_vdc_1 = ('''Ta có hiệu số đo giữa hai góc lượng giác là:\\\\
            $\\frac{%s\\pi}{%s} - \\left(-\\frac{\\pi}{%s}\\right) = \\frac{%s\\pi}{%s} = 3\\pi$.\\\\
            Vì hiệu số đo bằng $3\\pi = \\pi + 1 \\cdot 2\\pi$ (không chia hết cho $2\\pi$) nên hai góc lượng giác này không có cùng điểm biểu diễn trên đường tròn lượng giác.''' %(latex(tu_c3), latex(mau_c), latex(mau_c), latex(tu_c3 + 1), latex(mau_c)))
            list_vdc_2 = [loigiai_vdc_1]

            combined_vdc = list(zip(list_vdc_1, list_vdc_2))
            random.shuffle(combined_vdc)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Lặp đến khi đáp án có từ 1 đến 3 đúng để đảm bảo tính logic Đúng/Sai
            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)

                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                true_count = count_true_answers(answers)

                if 1 <= true_count <= 3:
                    break

            # Gán lại vào list sau khi lọc điều kiện số câu đúng hợp lệ
            list_nb_1 = [nb_da_1]
            list_th_1 = [th_da_1]
            list_vd_1 = [vd_da_1]
            list_vdc_1 = [vdc_da_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            combined_th = list(zip(list_th_1, list_th_2))
            combined_vd = list(zip(list_vd_1, list_vd_2))
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))

            random.shuffle(combined_nb)
            random.shuffle(combined_th)
            random.shuffle(combined_vd)
            random.shuffle(combined_vdc)

            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn theo đúng định dạng chuỗi %s
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+
            str(noidungcauhoi)+ '\n'
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

