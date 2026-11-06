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


def bt_dang43_p2_b2_c4_ds12(self):
            # Khai báo biến
            # Chọn k_pick bi từ hộp 2.

            x1 = random.randint(5, 7) # Số bi xanh hộp 1
            r1 = 1                     # Số bi đỏ hộp 1 (giữ cố định 1 để giống cấu trúc đề)
            n1 = x1 + r1               # Tổng bi hộp 1
            r2 = random.randint(3, 5) # Số bi đỏ hộp 2 ban đầu
            n_pick = 3                 # Số bi lấy từ hộp 1
            k_pick = 2                 # Số bi lấy từ hộp 2

            # Tính toán các giá trị xác suất và tổ hợp
            C_n1_3 = binomial(n1, n_pick)
            # Biến cố A: 3 bi lấy từ hộp 1 cùng màu (Vì r1=1 nên chỉ có thể là 3 xanh)
            C_x1_3 = binomial(x1, n_pick)
            pa = Rational(C_x1_3, C_n1_3)

            # Biến cố B: 2 bi lấy từ hộp 2 cùng màu
            # TH1: Lấy 3 xanh từ hộp 1. Xác suất pa.
            # Hộp 2 lúc này: 3 xanh, r2 đỏ. Tổng r2+3.
            pb_a = Rational(binomial(3, k_pick) + binomial(r2, k_pick), binomial(r2 + 3, k_pick))

            # TH2: Lấy 1 đỏ và 2 xanh từ hộp 1. Xác suất p_not_a.
            p_not_a = 1 - pa
            # Hộp 2 lúc này: 2 xanh, r2+1 đỏ. Tổng r2+3.
            pb_not_a = Rational(binomial(2, k_pick) + binomial(r2 + 1, k_pick), binomial(r2 + 3, k_pick))

            # Xác suất toàn phần P(B)
            pb = pa * pb_a + p_not_a * pb_not_a

            # Xác suất Bayes P(A|B)
            pa_b = (pa * pb_a) / pb

            # --- Nội dung câu hỏi ---
            noidungcauhoi = (r'''Hộp thứ nhất chứa %s viên bi xanh và %s viên bi đỏ. Hộp thứ hai chứa %s viên bi đỏ. Chọn ngẫu nhiên %s viên bi từ hộp thứ nhất và bỏ vào hộp thứ hai, rồi từ hộp thứ hai chọn ra ngẫu nhiên %s viên bi.''' 
                             % (latex(x1), latex(r1), latex(r2), latex(n_pick), latex(k_pick)))

            ########################################################################
            # Nhận biết (Câu a) ############################################
            nb_da_1_d = r'\True Xác suất để %s viên bi lấy ra từ hộp thứ nhất có cùng màu là $%s$' % (latex(n_pick), latex(pa))
            nb_da_1_s = r'Xác suất để %s viên bi lấy ra từ hộp thứ nhất có cùng màu là $%s$' % (latex(n_pick), latex(Rational(C_x1_3, C_n1_3+1)))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            loigiai_nb_1 = (r'''Gọi $A$ là biến cố: "%s viên bi lấy ra từ hộp thứ nhất có cùng màu". \\ Vì hộp thứ nhất chứa %s viên bi xanh và %s viên bi đỏ nên lấy %s viên bi cùng màu phải là %s bi xanh $\Rightarrow P(A) = \frac{C_{%s}^{%s}}{C_{%s}^{%s}} = %s$.''' 
                            % (latex(n_pick), latex(x1), latex(r1), latex(n_pick), latex(n_pick), latex(x1), latex(n_pick), latex(n1), latex(n_pick), latex(pa)))

            ########################################################################
            # Thông hiểu (Câu b) ############################################
            th_da_1_d = r'\True Xác suất để %s viên bi lấy ra từ hộp thứ hai có cùng màu là $%s$' % (latex(k_pick), latex(pb))
            th_da_1_s = r'Xác suất để %s viên bi lấy ra từ hộp thứ hai có cùng màu là $%s$' % (latex(k_pick), latex(Rational(pb.p + 1, pb.q)))
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            loigiai_th_1 = (r'''Gọi $B$ là biến cố: "%s viên bi lấy ra từ hộp thứ hai có cùng màu". \\ TH1: Lấy %s bi xanh từ hộp thứ nhất: $P(A)=%s$. Khi đó hộp thứ hai có %s bi đỏ và %s bi xanh $\Rightarrow P(B|A)=\frac{C_{%s}^{%s}+C_{%s}^{%s}}{C_{%s}^{%s}} = %s$. \\ TH2: Lấy %s bi đỏ và %s bi xanh từ hộp thứ nhất: $P(\overline{A})=1-%s=%s$. Khi đó hộp thứ hai có %s bi đỏ và %s bi xanh $\Rightarrow P(B|\overline{A})=\frac{C_{%s}^{%s}+C_{%s}^{%s}}{C_{%s}^{%s}} = %s$. \\ Theo công thức xác suất toàn phần: $P(B)=P(A).P(B|A)+P(\overline{A}).P(B|\overline{A}) = %s$.''' 
                            %(latex(k_pick), latex(n_pick), latex(pa), latex(r2), latex(n_pick), latex(r2), latex(k_pick), latex(n_pick), latex(k_pick), latex(r2+3), latex(k_pick), latex(pb_a), latex(r1), latex(n_pick-r1), latex(pa), latex(p_not_a), latex(r2+1), latex(n_pick-1), latex(r2+1), latex(k_pick), latex(n_pick-1), latex(k_pick), latex(r2+3), latex(k_pick), latex(pb_not_a), latex(pb)))

            ########################################################################
            # Vận dụng (Câu c) ############################################
            vd_da_1_d = r'\True Số cách chọn %s viên bi từ hộp thứ nhất là $C_{%s}^{%s}$' % (latex(n_pick), latex(n1), latex(n_pick))
            vd_da_1_s = r'Số cách chọn %s viên bi từ hộp thứ nhất là $C_{11}^{3}$' % (latex(n_pick))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            loigiai_vd_1 = (r'''Hộp thứ nhất chứa %s viên bi nên số cách chọn %s viên bi từ hộp thứ nhất là $C_{%s}^{%s}$.''' 
                            % (latex(n1), latex(n_pick), latex(n1), latex(n_pick)))

            ########################################################################
            # Vận dụng cao (Câu d) ############################################
            vdc_da_1_d = r'\True Biết %s viên bi lấy ra ở hộp thứ hai có cùng màu, xác suất %s viên bi lấy ra từ hộp thứ nhất có cùng màu bằng $%s$' % (latex(k_pick), latex(n_pick), latex(pa_b))
            vdc_da_1_s = r'Biết %s viên bi lấy ra ở hộp thứ hai có cùng màu, xác suất %s viên bi lấy ra từ hộp thứ nhất có cùng màu bằng $%s$' % (latex(k_pick), latex(n_pick), latex(Rational(1, 2)))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            loigiai_vdc_1 = (r'''Theo công thức Bayes, ta có: $P(A|B) = \frac{P(A).P(B|A)}{P(B)} = \frac{%s \cdot %s}{%s} = %s$.''' 
                             % (latex(pa), latex(pb_a), latex(pb), latex(pa_b)))

            # --- Logic chọn đáp án và xáo trộn (Giữ nguyên cấu trúc mẫu) ---
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)
                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                if 1 <= count_true_answers(answers) <= 3:
                    break

            # Gán lời giải tương ứng (Ở đây mỗi câu chỉ có 1 lời giải logic)
            shuffled_solutions = [loigiai_nb_1, loigiai_th_1, loigiai_vd_1, loigiai_vdc_1]
            shuffled_answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]

            # --- Xuất kết quả định dạng LaTeX ---
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + 
                str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(shuffled_answers[0]) + '}\n'
                '{' + str(shuffled_answers[1]) + '}\n'
                '{' + str(shuffled_answers[2]) + '}\n'
                '{' + str(shuffled_answers[3]) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(shuffled_solutions[0]) + '\n'
                '\\item ' + str(shuffled_solutions[1]) + '\n'
                '\\item ' + str(shuffled_solutions[2]) + '\n'
                '\\item ' + str(shuffled_solutions[3]) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

