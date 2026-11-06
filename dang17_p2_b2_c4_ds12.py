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


def bt_dang17_p2_b2_c4_ds12(self):
            # Khai báo biến
            # Hàm hỗ trợ chuyển đổi dấu chấm thành dấu phẩy và ép kiểu về chuỗi để đưa vào LaTeX
            def to_vn(value):
                if isinstance(value, float):
                    # Làm tròn 2 chữ số và thay . bằng ,
                    res = "{:.2f}".format(value).rstrip('0').rstrip('.')
                    return res.replace('.', ',')
                return str(value).replace('.', ',')

            # 1. Khai báo và Random các thông số bài toán
            n_total = 100 
            list_n_B = [70, 75, 80]
            n_B = random.choice(list_n_B)
            n_not_B = n_total - n_B

            # Tỉ lệ thực sự xem (A) khi biết trả lời (B hoặc không B)
            p_A_given_B = random.choice([0.8, 0.85, 0.9])
            p_A_given_not_B = random.choice([0.1, 0.15, 0.2])

            # Tính toán các giá trị số lượng người
            n_A_and_B = int(n_B * p_A_given_B)
            n_not_A_and_B = n_B - n_A_and_B

            n_A_and_not_B = int(n_not_B * p_A_given_not_B)
            n_not_A_and_not_B = n_not_B - n_A_and_not_B

            # Tổng số người thực sự xem
            n_A = n_A_and_B + n_A_and_not_B
            prob_A_val = n_A / n_total
            prob_AB_val = n_A_and_B / n_total

            # Phần mặc áo đội bóng (Câu d)
            n_shirt = 20
            n_shirt_watch = random.randint(12, 16)
            n_shirt_not_watch = n_shirt - n_shirt_watch
            rate_shirt_not_watch = int((n_shirt_not_watch / n_shirt) * 100)

            # Nội dung câu hỏi
            noidungcauhoi = ('''Trước $%s$ tiếng khi diễn ra trận Derby thành Manchester giữa MU-MC. Người ta phỏng vấn ngẫu nhiên $%s$ người hâm mộ của MU (có $%s$ người đang mặc áo của đội bóng) về việc có nên xem trận đấu đó hay không. Kết quả cho thấy rằng $%s$ người trả lời sẽ xem, $%s$ người trả lời sẽ không xem. Nhưng thực tế cho thấy rằng tỉ lệ người hâm mộ MU thực sự xem trận đấu tương ứng với những cách trả lời “có xem” và “không xem” là $%s\\%%$ và $%s\\%%$.
            Gọi $A$ là biến cố “Người được phỏng vấn thực sự sẽ xem trận đấu”.
            Gọi $B$ là biến cố “Người được phỏng vấn trả lời sẽ xem trận đấu”.''' 
            %(3, n_total, n_shirt, n_B, n_not_B, to_vn(int(p_A_given_B*100)), to_vn(int(p_A_given_not_B*100))))

            ########################################################################
            # Nhận biết (Câu a) ############################################
            val_a_true = to_vn(prob_AB_val)
            val_a_false = to_vn(round(prob_AB_val + 0.1, 1))

            nb_da_1_d = '\\True $P(AB) = %s$' % val_a_true
            nb_da_1_s = '$P(AB) = %s$' % val_a_false
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            # Lời giải a với bảng TikZ
            loigiai_nb_1 = ('''Từ bài ra, ta có bảng sau: \\\\
            \\begin{tikzpicture}[font=\\footnotesize, x=1cm, y=0.8cm]
                \\draw (0,0) rectangle (13,3);
                \\draw (0,1) -- (13,1); 
                \\draw (0,2) -- (13,2);
                \\draw (5,0) -- (5,3); 
                \\draw (9,0) -- (9,3);
                \\draw (0,3) -- (5,2);
                \\node at (1.5,2.2) {Phỏng vấn}; 
                \\node at (3.5,2.8) {Thực tế};
                \\node at (7,2.5) {Người xem thật}; 
                \\node at (11,2.5) {Người không xem thật};
                \\node at (2.5,1.5) {Người trả lời xem ($%s$)};
                \\node at (7,1.5) {$%s \\cdot %s = %s$};
                \\node at (11,1.5) {$%s - %s = %s$};
                \\node at (2.5,0.5) {Người trả lời không xem ($%s$)};
                \\node at (7,0.5) {$%s \\cdot %s = %s$};
                \\node at (11,0.5) {$%s - %s = %s$};
            \\end{tikzpicture} \\\\
            $AB$ là tập hợp người được phỏng vấn trả lời sẽ xem và xem thật, do đó $n(AB) = %s$. \\\\
            Vậy $P(AB) = \\frac{%s}{%s} = %s$.''' 
            %(n_B, to_vn(p_A_given_B), n_B, n_A_and_B, n_B, n_A_and_B, n_not_A_and_B,
              n_not_B, to_vn(p_A_given_not_B), n_not_B, n_A_and_not_B, n_not_B, n_A_and_not_B, n_not_A_and_not_B,
              n_A_and_B, n_A_and_B, n_total, val_a_true))

            ########################################################################
            # Thông hiểu (Câu b) ############################################
            val_b_true = to_vn(prob_A_val * 100)
            val_b_false = to_vn(72.5)

            th_da_1_d = '\\True Tỉ lệ người được phỏng vấn thực sự sẽ xem trận đấu là $%s\\%%$' % val_b_true
            th_da_1_s = 'Tỉ lệ người được phỏng vấn thực sự sẽ xem trận đấu là $%s\\%%$' % val_b_false
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            loigiai_th_1 = ('''$A$ là tập hợp người được phỏng vấn xem thật trận đấu nên $n(A) = %s + %s = %s$, do đó $P(A) = \\frac{%s}{%s} = %s$. Vậy tỉ lệ người được phỏng vấn thực sự sẽ xem trận đấu là $%s\\%%$. \\\\
            Ngoài ra, ta có thể thực hiện tìm $P(A)$ theo công thức xác suất toàn phần như sau: \\\\
            Theo bài ra ta có: $P(B) = %s$; $P(\\bar{B}) = %s$; $P(A|B) = %s$; $P(A|\\bar{B}) = %s$. \\\\
            Do đó, $P(A) = P(B) \\cdot P(A|B) + P(\\bar{B}) \\cdot P(A|\\bar{B}) = %s \\cdot %s + %s \\cdot %s = %s$.''' 
            %(n_A_and_B, n_A_and_not_B, n_A, n_A, n_total, to_vn(prob_A_val), val_b_true,
              to_vn(n_B/n_total), to_vn(n_not_B/n_total), to_vn(p_A_given_B), to_vn(p_A_given_not_B),
              to_vn(n_B/n_total), to_vn(p_A_given_B), to_vn(n_not_B/n_total), to_vn(p_A_given_not_B), to_vn(prob_A_val)))

            ########################################################################
            # Vận dụng (Câu c) ############################################
            rate_c = round((n_A_and_not_B / n_A) * 100, 2)
            val_c_true = to_vn(rate_c)
            val_c_false = to_vn(17)

            vd_da_1_d = '\\True Trong số người được phỏng vấn thực sự sẽ xem có $%s\\%%$ người trả lời không xem khi được phỏng vấn' % val_c_true
            vd_da_1_s = 'Trong số người được phỏng vấn thực sự sẽ xem có $%s\\%%$ người trả lời không xem khi được phỏng vấn' % val_c_false
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            loigiai_vd_1 = ('''Tổng số người được phỏng vấn thực sự sẽ xem thật trận đấu là $%s$ người. Số người trả lời không xem khi được phỏng vấn là $%s$ người. \\\\
            Tỉ lệ người trả lời không xem khi được phỏng vấn trong số những người thực sự xem trận đấu là $\\frac{%s}{%s} \\approx %s\\%%$.''' 
            %(n_A, n_A_and_not_B, n_A_and_not_B, n_A, val_c_true))

            ########################################################################
            # Vận dụng cao (Câu d) ############################################
            vdc_da_1_d = '\\True Trong số những người mặc áo đội bóng có $%s\\%%$ người phỏng vấn thực sự sẽ không xem trận đấu biết rằng số người được phỏng vấn thực sự sẽ xem trận đấu mặc áo đội bóng là $%s$ người' % (to_vn(rate_shirt_not_watch), n_shirt_watch)
            vdc_da_1_s = 'Trong số những người mặc áo đội bóng có $%s\\%%$ người phỏng vấn thực sự sẽ không xem trận đấu biết rằng số người được phỏng vấn thực sự sẽ xem trận đấu mặc áo đội bóng là $%s$ người' % (30, n_shirt_watch)
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            loigiai_vdc_1 = ('''Tỉ lệ người phỏng vấn thực sự sẽ không xem trận đấu trong số những người mặc áo đội bóng là $\\frac{%s - %s}{%s} = %s\\%%$.''' 
            %(n_shirt, n_shirt_watch, n_shirt, to_vn(rate_shirt_not_watch)))

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Lặp chọn bộ đáp án
            while True:
                ans_a = random.choice(list_nb_da_1)
                ans_b = random.choice(list_th_da_1)
                ans_c = random.choice(list_vd_da_1)
                ans_d = random.choice(list_vdc_da_1)
                if 1 <= count_true_answers([ans_a, ans_b, ans_c, ans_d]) <= 3:
                    break

            # Xuất Content
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(ans_a) + '}\n'
                '{' + str(ans_b) + '}\n'
                '{' + str(ans_c) + '}\n'
                '{' + str(ans_d) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(loigiai_nb_1) + '\n'
                '\\item ' + str(loigiai_th_1) + '\n'
                '\\item ' + str(loigiai_vd_1) + '\n'
                '\\item ' + str(loigiai_vdc_1) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

