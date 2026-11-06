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


def bt_dang36_p2_b3_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến ký hiệu
            n = symbols('n')

            # B3: Suy nghĩ tìm cách random bài toán
            # Trọng lượng trung bình: P(n) = A - Bn
            # Để kết quả đẹp: n_max = A/(2B) phải là số nguyên. 
            # Do đó A phải chia hết cho 2B.
            B = random.choice([10, 20, 30])
            k = random.randint(10, 15) # k chính là n_max (hoành độ đỉnh)
            A = 2 * B * k 

            # Hàm trọng lượng trung bình: P(n) = A - Bn
            Pn = A - B * n
            # Hàm tổng trọng lượng: f(n) = n * P(n) = -B*n^2 + A*n
            fn = -B * n**2 + A * n

            # Giá trị cực đại theo tính chất Parabol
            n_max = k
            f_max = fn.subs(n, n_max)

            # Giới hạn số lượng cá để P(n) > 0
            n_limit = A // B

            # Thông số cho câu d (bất phương trình f(n) >= K)
            n_target = random.randint(4, k - 2)
            K_value = int(fn.subs(n, n_target))

            # Nội dung câu hỏi
            noidungcauhoi = ('''Một người nuôi cá thí nghiệm trong hồ. Người đó thấy rằng nếu mỗi đơn vị diện tích của mặt hồ có $n$ con cá thì trung bình mỗi con cá sau một vụ cân nặng $P(n) = %s - %s n$ (gam). Xét tính đúng, sai của các khẳng định sau:''' 
                             % (latex(A), latex(B)))

            ########################################################################
            # Nhận biết: Về điều kiện thực tế của n (P(n) > 0)
            nb_da_1_d = '\\True Không thể thả quá %s con cá trên một đơn vị diện tích mặt hồ' % (latex(n_limit))
            nb_da_1_s = 'Có thể thả tùy ý số lượng cá trên một đơn vị diện tích mà trọng lượng cá vẫn không đổi'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            list_nb_1 = [nb_da_1]
            loigiai_nb_1 = ('''Trọng lượng trung bình của mỗi con cá phải là số dương, do đó: \\\\ $P(n) > 0 \\Leftrightarrow %s - %s n > 0 \\Leftrightarrow n < %s$. \\\\ Vậy không thể thả quá %s con cá trên một đơn vị diện tích.''' 
                            % (latex(A), latex(B), latex(n_limit), latex(n_limit)))
            list_nb_2 = [loigiai_nb_1]

            ########################################################################
            # Thông hiểu: Công thức tính tổng trọng lượng
            th_da_1_d = '\\True Tổng trọng lượng cá thu được trên một đơn vị diện tích là $f(n) = -%s n^2 + %s n$ (gam)' % (latex(B), latex(A))
            th_da_1_s = 'Tổng trọng lượng cá thu được trên một đơn vị diện tích là $f(n) = -%s n^2 + %s n$ (gam)' % (latex(B//2), latex(A))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            list_th_1 = [th_da_1]
            loigiai_th_1 = ('''Gọi $f(n)$ là tổng trọng lượng cá thu được trên một đơn vị diện tích. \\\\ Ta có $f(n) = n \\cdot P(n) = n(%s - %s n) = -%s n^2 + %s n$ (gam).''' 
                            % (latex(A), latex(B), latex(B), latex(A)))
            list_th_2 = [loigiai_th_1]

            ########################################################################
            # Vận dụng: Tìm giá trị lớn nhất bằng tính chất hàm bậc hai (Parabol)
            vd_da_1_d = '\\True Tổng trọng lượng cá trên một đơn vị diện tích đạt tối đa là %s gam' % (latex(f_max))
            vd_da_1_s = 'Tổng trọng lượng cá trên một đơn vị diện tích đạt tối đa là %s gam' % (latex(f_max + 100))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            list_vd_1 = [vd_da_1]
            loigiai_vd_1 = ('''Hàm số $f(n) = -%s n^2 + %s n$ là hàm số bậc hai với hệ số $a = -%s, b = %s$. \\\\ Vì $a < 0$ nên đồ thị hàm số là một parabol có bề lõm quay xuống dưới. \\\\ Hàm số đạt giá trị lớn nhất tại hoành độ đỉnh: $n_0 = -\\frac{b}{2a} = -\\frac{%s}{2 \\cdot (-%s)} = %s$. \\\\ Giá trị lớn nhất đó là $f(%s) = -%s \\cdot (%s)^2 + %s \\cdot %s = %s$ (gam).''' 
                            % (latex(B), latex(A), latex(B), latex(A), latex(A), latex(B), latex(n_max), latex(n_max), latex(B), latex(n_max), latex(A), latex(n_max), latex(f_max)))
            list_vd_2 = [loigiai_vd_1]

            ########################################################################
            # Vận dụng cao: Bài toán thực tế về sản lượng tối thiểu
            vdc_da_1_d = '\\True Có thể thả ít nhất %s con cá trên một đơn vị diện tích để thu hoạch được tối thiểu %s gam cá' % (latex(n_target), latex(K_value))
            vdc_da_1_s = 'Chỉ có duy nhất một cách thả %s con cá mới thu được sản lượng trên %s gam' % (latex(n_max), latex(K_value))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            list_vdc_1 = [vdc_da_1]
            loigiai_vdc_1 = ('''Để sản lượng thu hoạch đạt tối thiểu %s gam, ta cần giải bất phương trình: \\\\ $f(n) \\ge %s \\Leftrightarrow -%s n^2 + %s n \\ge %s \\Leftrightarrow %s n^2 - %s n + %s \\le 0$. \\\\ Với $n = %s$, ta có $f(%s) = %s \\ge %s$. Vậy có thể thả ít nhất %s con cá để thỏa mãn yêu cầu.''' 
                             % (latex(K_value), latex(K_value), latex(B), latex(A), latex(K_value), latex(B), latex(A), latex(K_value), latex(n_target), latex(n_target), latex(K_value), latex(K_value), latex(n_target)))
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

            list_nb_1, list_th_1, list_vd_1, list_vdc_1 = [nb_da_1], [th_da_1], [vd_da_1], [vdc_da_1]
            combined_nb = list(zip(list_nb_1, list_nb_2))
            combined_th = list(zip(list_th_1, list_th_2))
            combined_vd = list(zip(list_vd_1, list_vd_2))
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))

            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            # Xuất nội dung LaTeX
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

