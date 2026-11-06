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


def bt_dang12_p2_b2_c6_ds10(self):
            # Khai báo biến
            # Khai báo biến và tạo ngẫu nhiên số liệu
            N = random.choice([10000, 20000, 50000]) # Tổng số người
            rate_A = random.choice([0.1, 0.2])
            A = int(N * rate_A) # Số người nhận cảnh báo
            not_A = N - A # Số người không nhận cảnh báo

            rate_B_in_A = random.choice([0.6, 0.7, 0.8])
            B = int(A * rate_B_in_A) # Có bệnh trong nhóm nhận cảnh báo
            not_B = A - B # Không bệnh trong nhóm nhận cảnh báo

            rate_C_in_not_A = random.choice([0.01, 0.02, 0.05])
            C = int(not_A * rate_C_in_not_A) # Có bệnh trong nhóm KHÔNG nhận cảnh báo
            not_C = not_A - C # Không bệnh trong nhóm KHÔNG nhận cảnh báo

            total_not_D = not_B + not_C # Tổng số người KHÔNG bệnh
            total_D = B + C # Tổng số người CÓ bệnh

            # Nội dung câu hỏi
            noidungcauhoi = ('''Nhằm đưa ra cảnh báo sớm về tình trạng sức khỏe của cư dân, người ta sử dụng một ứng dụng trí tuệ nhân tạo để sàng lọc nguy cơ mắc bệnh dựa trên hồ sơ y tế được lưu trữ. Khi phát hiện nguy cơ mắc bệnh, ứng dụng này sẽ gửi cảnh báo để giúp người dân đi khám bệnh kịp thời. Người ta dùng ứng dụng này để tầm soát nguy cơ mắc một loại bệnh.\\\\Kết quả thu được khi quét thử nghiệm hồ sơ y tế của $%s$ người như sau: Có $%s$ người nhận được cảnh báo và $%s$ người còn lại không nhận được cảnh báo từ ứng dụng. Trong số $%s$ người nhận được cảnh báo thì có $%s$ người có bệnh và $%s$ người không có bệnh. Trong số $%s$ người không nhận được cảnh báo thì có $%s$ người có bệnh và $%s$ người không có bệnh. \\\\Chọn ngẫu nhiên một người trong số $%s$ người nói trên.''' 
                             % (N, A, not_A, A, B, not_B, not_A, C, not_C, N))

            ######################################################################## Nhận biết ############################################

            # Tính toán câu a
            p_a_val = round(not_A / N, 2)
            p_a_false_val = round(p_a_val - 0.1, 2)

            # Các đáp án
            nb_da_1_d = '\\True Xác suất để người đó không nhận được cảnh báo từ ứng dụng bằng $%s$' % str(p_a_val).replace('.', ',')
            nb_da_1_s = 'Xác suất để người đó không nhận được cảnh báo từ ứng dụng bằng $%s$' % str(p_a_false_val).replace('.', ',')
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Gọi $X$ là biến cố "Người đó không nhận được cảnh báo từ ứng dụng". \\\\Số kết quả thuận lợi cho $X$ là $n(X) = %s$. Tổng số kết quả có thể xảy ra là $n(\\Omega) = %s$. \\\\Xác suất cần tìm là $P(X) = \\frac{%s}{%s} = %s$.''' % (not_A, N, not_A, N, str(p_a_val).replace('.', ',')))
            list_nb_2 = [loigiai_nb_1]

            ######################################################################## Thông hiểu ############################################

            # Tính toán câu b: P(Không bệnh | Không cảnh báo)
            val_b = not_C / not_A
            b_thresh = round(val_b - 0.005, 2) # Tạo mốc so sánh (vd thực tế là 0.988 thì lấy mốc 0.98)

            # Các đáp án
            th_da_1_d = '\\True Xác suất để người đó không có bệnh, biết rằng người đó không nhận được cảnh báo từ ứng dụng, lớn hơn $%s$' % str(b_thresh).replace('.', ',')
            th_da_1_s = 'Xác suất để người đó không có bệnh, biết rằng người đó không nhận được cảnh báo từ ứng dụng, nhỏ hơn $%s$' % str(b_thresh).replace('.', ',')
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            # Nội dung lời giải
            loigiai_th_1 = ('''Xác suất để người đó không có bệnh, biết rằng người đó không nhận được cảnh báo từ ứng dụng là xác suất có điều kiện: \\\\ $P = \\frac{%s}{%s} \\approx %s > %s$.''' % (not_C, not_A, str(round(val_b, 4)).replace('.', ','), str(b_thresh).replace('.', ',')))
            list_th_2 = [loigiai_th_1]

            ######################################################################## Vận dụng ############################################

            # Tính toán câu c: P(Không bệnh)
            p_c_val = round(total_not_D / N, 2)
            p_c_false_val = round(p_c_val - 0.02, 2)

            # Các đáp án
            vd_da_1_d = '\\True Xác suất để người đó không có bệnh bằng $%s$' % str(p_c_val).replace('.', ',')
            vd_da_1_s = 'Xác suất để người đó không có bệnh bằng $%s$' % str(p_c_false_val).replace('.', ',')
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Tổng số người không có bệnh là: $%s + %s = %s$ người. \\\\Xác suất để người đó không có bệnh là: $P = \\frac{%s}{%s} = %s$.''' % (not_B, not_C, total_not_D, total_not_D, N, str(p_c_val).replace('.', ',')))
            list_vd_2 = [loigiai_vd_1]

            ######################################################################## Vận dụng cao ############################################

            # Tính toán câu d: P(Không cảnh báo | Không bệnh)
            val_d = not_C / total_not_D
            d_thresh = round(val_d - 0.015, 2)

            # Các đáp án
            vdc_da_1_d = '\\True Xác suất để người đó không nhận được cảnh báo từ ứng dụng, biết rằng người đó không có bệnh, lớn hơn $%s$' % str(d_thresh).replace('.', ',')
            vdc_da_1_s = 'Xác suất để người đó không nhận được cảnh báo từ ứng dụng, biết rằng người đó không có bệnh, nhỏ hơn $%s$' % str(d_thresh).replace('.', ',')
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Xác suất để người đó không nhận được cảnh báo từ ứng dụng, biết rằng người đó không có bệnh là xác suất có điều kiện: \\\\ $P = \\frac{%s}{%s} \\approx %s > %s$.''' % (not_C, total_not_D, str(round(val_d, 4)).replace('.', ','), str(d_thresh).replace('.', ',')))
            list_vdc_2 = [loigiai_vdc_1]

            ######################################################################## Trộn và xuất ############################################

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

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
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
                       '\\end{ex}\n\\end{minipage}\n\n')
            return content

