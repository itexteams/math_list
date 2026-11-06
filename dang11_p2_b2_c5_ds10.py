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


def bt_dang11_p2_b2_c5_ds10(self):
            # Khai báo biến
            # Khai báo biến
            # Random số lượng người tổng (N) và số người cần chọn (K)
            N = random.randint(13, 15)
            K = random.randint(5, 6)

            # Tính toán các giá trị tổ hợp chính xác
            val_a = math.comb(N, K)
            val_b = math.comb(N - 2, K - 2)
            val_c = math.comb(N - 2, K)
            # Câu d: Chọn nhóm K người có (A hoặc B), sau đó chọn 1 người làm tổ trưởng
            # Số cách chọn nhóm K người có mặt đúng 1 trong 2 người A, B: 2 * C(N-2, K-1)
            # Mỗi nhóm có K cách chọn tổ trưởng
            val_d = 2 * math.comb(N - 2, K - 1) * K

            # Nội dung câu hỏi
            noidungcauhoi = ('''Một tập thể có $%s$ người trong đó có hai bạn tên $A$ và $B$. Người ta cần chọn một tổ công tác gồm $%s$ người.''' 
                             %(str(N), str(K)))

            ########################################################################
            # Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Chọn nhóm $%s$ bạn bất kỳ ta có $%s$ cách' % (str(K), str(val_a))
            nb_da_1_s = 'Chọn nhóm $%s$ bạn bất kỳ ta có $%s$ cách' % (str(K), str(val_a + 100))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            # Nội dung lời giải
            loigiai_nb_1 = ('''Số cách chọn $%s$ người bất kỳ từ $%s$ người là $C_{%s}^{%s} = %s$ cách.''' 
                            %(str(K), str(N), str(N), str(K), str(val_a)))

            list_nb_1 = [nb_da_1]
            list_nb_2 = [loigiai_nb_1]
            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu ############################################
            # Các đáp án
            th_da_1_d = '\\True Chọn nhóm $%s$ bạn trong đó có cả $A$ và $B$, có $%s$ cách' % (str(K), str(val_b))
            th_da_1_s = 'Chọn nhóm $%s$ bạn trong đó có cả $A$ và $B$, có $%s$ cách' % (str(K), str(val_b + 50))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            # Nội dung lời giải
            loigiai_th_1 = ('''Để chọn nhóm có cả $A$ và $B$, ta lấy cố định $A, B$. Cần chọn thêm $%s$ người từ $%s$ người còn lại.\\\\ Số cách là $C_{%s}^{%s} = %s$ cách.''' 
                            %(str(K-2), str(N-2), str(N-2), str(K-2), str(val_b)))

            list_th_1 = [th_da_1]
            list_th_2 = [loigiai_th_1]
            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ########################################################################
            # Vận dụng ############################################
            # Các đáp án
            vd_da_1_d = '\\True Chọn nhóm $%s$ bạn trong đó không có hai bạn $A$ và $B$, có $%s$ cách' % (str(K), str(val_c))
            vd_da_1_s = 'Chọn nhóm $%s$ bạn trong đó không có hai bạn $A$ và $B$, có $%s$ cách' % (str(K), str(val_c - 20))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            # Nội dung lời giải
            loigiai_vd_1 = ('''Để chọn nhóm không có $A$ và $B$, ta chọn $%s$ người từ $%s$ người còn lại (loại $A, B$).\\\\ Số cách là $C_{%s}^{%s} = %s$ cách.''' 
                            %(str(K), str(N-2), str(N-2), str(K), str(val_c)))

            list_vd_1 = [vd_da_1]
            list_vd_2 = [loigiai_vd_1]
            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ########################################################################
            # Vận dụng cao ############################################
            # Các đáp án
            vdc_da_1_d = '\\True Có $%s$ cách chọn sao cho trong tổ phải có $1$ tổ trưởng và $%s$ tổ viên, hơn nữa $A$ hoặc $B$ phải có mặt nhưng không đồng thời cả hai' % (str(val_d), str(K-1))
            vdc_da_1_s = 'Có $%s$ cách chọn sao cho trong tổ phải có $1$ tổ trưởng và $%s$ tổ viên, hơn nữa $A$ hoặc $B$ phải có mặt nhưng không đồng thời cả hai' % (str(val_d // 2), str(K-1))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Bước 1: Chọn nhóm $%s$ người thỏa mãn chỉ có $A$ hoặc chỉ có $B$.\\\\
                            Trường hợp 1: Có $A$, không có $B$. Chọn $A$ và $%s$ người từ $%s$ người còn lại: $C_{%s}^{%s}$ cách.\\\\
                            Trường hợp 2: Có $B$, không có $A$. Chọn $B$ và $%s$ người từ $%s$ người còn lại: $C_{%s}^{%s}$ cách.\\\\
                            Tổng số cách chọn nhóm là $2 \\cdot C_{%s}^{%s} = 2 \\cdot %s = %s$ cách.\\\\
                            Bước 2: Với mỗi nhóm $%s$ người, chọn $1$ người làm tổ trưởng, $%s$ người còn lại là tổ viên: có $%s$ cách.\\\\
                            Vậy tổng số cách là $%s \\cdot %s = %s$ cách.''' 
                            %(str(K), str(K-1), str(N-2), str(N-2), str(K-1), str(K-1), str(N-2), str(N-2), str(K-1), str(N-2), str(K-1), str(math.comb(N-2, K-1)), str(2 * math.comb(N-2, K-1)), str(K), str(K-1), str(K), str(2 * math.comb(N-2, K-1)), str(K), str(val_d)))

            list_vdc_1 = [vdc_da_1]
            list_vdc_2 = [loigiai_vdc_1]
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))
            random.shuffle(combined_vdc)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

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

            # Gán lại vào list
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

            # Xuất câu hỏi
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

