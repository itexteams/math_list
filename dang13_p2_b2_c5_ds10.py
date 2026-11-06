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


def bt_dang13_p2_b2_c5_ds10(self):
            # Khai báo biến
            # Khai báo biến ngẫu nhiên cho bài toán
            # nA: số học sinh lớp 12A, nB: số học sinh lớp 12B, nC: số học sinh lớp 12C
            # k: số học sinh cần chọn
            nA = random.randint(4, 5)
            nB = random.randint(3, 4)
            nC = 2
            k = 5
            tong_hs = nA + nB + nC

            # Các tính toán tổ hợp
            def nCr(n, r):
                if r > n or r < 0:
                    return 0
                return math.comb(n, r)

            total_ways = nCr(tong_hs, k)
            ways_AB = nCr(nA + nB, k)
            ways_BC = nCr(nB + nC, k)
            ways_AC = nCr(nA + nC, k)

            # Tính số cách chọn sao cho lớp nào cũng có học sinh (Bao hàm - Loại trừ)
            # Cách chọn ít nhất 1 học sinh mỗi lớp = Tổng - (Thiếu ít nhất 1 lớp)
            # = Total - (Cách chọn ko có A + ko có B + ko có C) + (Chỉ có A + Chỉ có B + Chỉ có C)
            missing_A = nCr(nB + nC, k)
            missing_B = nCr(nA + nC, k)
            missing_C = nCr(nA + nB, k)
            only_A = nCr(nA, k)
            only_B = nCr(nB, k)
            only_C = nCr(nC, k)
            at_least_one_each = total_ways - (missing_A + missing_B + missing_C) + (only_A + only_B + only_C)

            # Nội dung câu hỏi
            noidungcauhoi = ('''Đội văn nghệ của nhà trường gồm %s học sinh lớp $12A$, %s học sinh lớp $12B$ và %s học sinh lớp $12C$. Chọn ngẫu nhiên %s học sinh từ đội văn nghệ để biểu diễn trong lễ bế giảng.''' 
                             %(latex(nA), latex(nB), latex(nC), latex(k)))

            ########################################################################
            # Nhận biết ############################################
            nb_da_1_d = '\\True Chọn %s học sinh tùy ý từ %s học sinh có: %s cách' % (latex(k), latex(tong_hs), latex(total_ways))
            nb_da_1_s = 'Chọn %s học sinh tùy ý từ %s học sinh có: %s cách' % (latex(k), latex(tong_hs), latex(total_ways + random.randint(5, 15)))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            loigiai_nb_1 = ('''Số cách chọn %s học sinh tùy ý từ %s học sinh là $C_{%s}^{%s} = %s$ cách.''' 
                            % (latex(k), latex(tong_hs), latex(tong_hs), latex(k), latex(total_ways)))

            list_nb_2 = [loigiai_nb_1]

            ########################################################################
            # Thông hiểu ############################################
            th_da_1_d = '\\True Chọn %s học sinh chỉ từ lớp $12A$ và $12B$ có: %s cách' % (latex(k), latex(ways_AB))
            th_da_1_s = 'Chọn %s học sinh chỉ từ lớp $12A$ và $12B$ có: %s cách' % (latex(k), latex(ways_AB + 5))
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            loigiai_th_1 = ('''Số học sinh lớp $12A$ và $12B$ là $%s + %s = %s$ học sinh. \\\\ 
            Số cách chọn %s học sinh từ %s học sinh này là $C_{%s}^{%s} = %s$ cách.''' 
                            % (latex(nA), latex(nB), latex(nA + nB), latex(k), latex(nA + nB), latex(nA + nB), latex(k), latex(ways_AB)))

            list_th_2 = [loigiai_th_1]

            ########################################################################
            # Vận dụng ############################################
            vd_da_1_d = '\\True Chọn %s học sinh chỉ từ lớp $12B$ và $12C$ có: %s cách' % (latex(k), latex(ways_BC))
            vd_da_1_s = 'Chọn %s học sinh chỉ từ lớp $12B$ và $12C$ có: %s cách' % (latex(k), latex(ways_BC + 1))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            loigiai_vd_1 = ('''Số học sinh lớp $12B$ và $12C$ là $%s + %s = %s$ học sinh. \\\\ 
            Số cách chọn %s học sinh từ %s học sinh này là $C_{%s}^{%s} = %s$ cách.''' 
                            % (latex(nB), latex(nC), latex(nB + nC), latex(k), latex(nB + nC), latex(nB + nC), latex(k), latex(ways_BC)))

            list_vd_2 = [loigiai_vd_1]

            ########################################################################
            # Vận dụng cao ############################################
            vdc_da_1_d = '\\True Có %s cách chọn sao cho lớp nào cũng có học sinh được chọn' % (latex(at_least_one_each))
            vdc_da_1_s = 'Có %s cách chọn sao cho lớp nào cũng có học sinh được chọn' % (latex(at_least_one_each - 8))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            loigiai_vdc_1 = ('''Sử dụng phương pháp phần bù: \\\\ 
            - Số cách chọn không có học sinh lớp $12A$ (chọn từ $12B, 12C$): $C_{%s}^{%s} = %s$. \\\\ 
            - Số cách chọn không có học sinh lớp $12B$ (chọn từ $12A, 12C$): $C_{%s}^{%s} = %s$. \\\\ 
            - Số cách chọn không có học sinh lớp $12C$ (chọn từ $12A, 12B$): $C_{%s}^{%s} = %s$. \\\\ 
            Lưu ý các trường hợp chỉ có học sinh của 1 lớp duy nhất (nếu có). \\\\ 
            Số cách chọn thỏa mãn lớp nào cũng có học sinh là: $%s - \\left( %s + %s + %s \\right) + \\left( %s + %s + %s \\right) = %s$ cách.''' 
                             % (latex(nB+nC), latex(k), latex(missing_A), 
                                latex(nA+nC), latex(k), latex(missing_B), 
                                latex(nA+nB), latex(k), latex(missing_C),
                                latex(total_ways), latex(missing_A), latex(missing_B), latex(missing_C),
                                latex(only_A), latex(only_B), latex(only_C), latex(at_least_one_each)))

            list_vdc_2 = [loigiai_vdc_1]

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

            # Gán lại vào list để xuất
            final_answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
            final_solutions = [loigiai_nb_1, loigiai_th_1, loigiai_vd_1, loigiai_vdc_1]

            # Xuất câu hỏi
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+
                str(noidungcauhoi)+ 
                '\\choiceTFn \n'
                '{'+str(final_answers[0])+'}\n'
                '{'+str(final_answers[1])+'}\n'
                '{'+str(final_answers[2])+'}\n'
                '{'+str(final_answers[3])+'}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(final_solutions[0])+'\n'
                '\\item '+str(final_solutions[1])+'\n'
                '\\item '+str(final_solutions[2])+'\n'
                '\\item '+str(final_solutions[3])+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

