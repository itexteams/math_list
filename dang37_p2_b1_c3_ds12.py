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


def bt_dang37_p2_b1_c3_ds12(self):
            # Khai báo biến ký hiệu
            t = symbols('t')

            # --- HÀM HỖ TRỢ ---
            def format_vn(value, precision=1):
                """Định dạng số thập phân dùng dấu phẩy và làm tròn."""
                num = round(float(value), precision)
                if num == int(num):
                    return str(int(num))
                return str(num).replace('.', ',')

            def count_true_answers(answers):
                """Đếm số lượng đáp án đúng trong danh sách."""
                return sum(1 for ans in answers if '\\True' in ans)

            # --- BƯỚC 1: RANDOM DỮ LIỆU GỐC ---
            v0 = random.choice([4, 6, 8, 10])
            list_a = [0.5, 1, 1.5, 2]
            a_val = random.choice([x for x in list_a if (v0/x).is_integer()])

            vt = -nsimplify(a_val) * t + v0
            st = integrate(vt, t)
            t_stop = int(v0 / a_val) 
            s_stop = nsimplify(st.subs(t, t_stop))

            # Nội dung câu hỏi (Dùng {{ }} cho LaTeX \text{...})
            noidungcauhoi = (f"Chị Loan đang lái xe với vận tốc ${latex(v0)}\\,\\text{{m/s}}$ thì nhận thấy phía trước đèn giao thông đang chuẩn bị chuyển sang đèn đỏ nên cần giảm tốc độ của xe để đợi đèn đỏ. "
                             f"Sau khi đạp phanh, xe chuyển động thẳng từ gốc $O$ theo trục $Ox$ ($O$ là gốc ứng với thời điểm vận tốc của xe là ${latex(v0)}\\,\\text{{m/s}}$) "
                             f"với vận tốc $v(t) = {latex(vt)}\\,(\\text{{m/s}})$, trong đó $t$ là thời gian tính bằng giây kể từ lúc chị Loan đạp phanh. "
                             f"Xét tính đúng sai của các mệnh đề sau:")

            # --- BƯỚC 2: CHUẨN BỊ CÁC LỰA CHỌN ĐÚNG/SAI (GIỮ NGUYÊN LỜI GIẢI) ---

            # a) Nhận biết
            lg_a = f"Quãng đường xe đi được sau $t$ giây kể từ lúc đạp phanh là:\\\\ $s(t) = \\int_0^t v(u) du = \\int_0^t ({latex(vt).replace('t', 'u')}) du = {latex(st)}$."
            list_da_a = [
                f"\\True Quãng đường xe đi được sau $t$ giây là $s(t) = {latex(st)}$",
                f"Quãng đường xe đi được sau $t$ giây là $s(t) = {latex(vt)}$"
            ]

            # b) Thông hiểu
            lg_b = f"Xe dừng hẳn khi $v(t) = 0 \\Leftrightarrow {latex(vt)} = 0 \\Leftrightarrow t = {latex(t_stop)}$ (giây)."
            list_da_b = [
                f"\\True Xe dừng hẳn sau ${latex(t_stop)}$ giây kể từ lúc đạp phanh",
                f"Xe dừng hẳn sau ${latex(v0)}$ giây kể từ lúc đạp phanh"
            ]

            # c) Vận dụng
            lg_c = f"Quãng đường xe đi được đến khi dừng hẳn là: $s = s({latex(t_stop)}) = {latex(s_stop)}$ (mét)."
            list_da_c = [
                f"\\True Quãng đường xe di chuyển được kể từ khi đạp phanh đến khi dừng hẳn là ${latex(s_stop)}\\,\\text{{m}}$",
                f"Quãng đường xe di chuyển được kể từ khi đạp phanh đến khi dừng hẳn là ${latex(nsimplify(s_stop + 2))}\\,\\text{{m}}$"
            ]

            # d) Vận dụng cao
            lg_d = f"Để xe dừng đúng quy định (không vượt quá vạch), khoảng cách từ xe đến vạch dừng tại thời điểm bắt đầu đạp phanh phải lớn hơn hoặc bằng quãng đường xe đi được cho đến khi dừng hẳn. Vậy xe phải cách vạch ít nhất ${latex(s_stop)}$ mét."
            list_da_d = [
                f"\\True Để dừng đúng quy định, lúc đạp phanh xe phải cách vạch dừng ít nhất ${latex(s_stop)}\\,\\text{{m}}$",
                f"Để dừng đúng quy định, lúc đạp phanh xe phải cách vạch dừng ít nhất ${latex(int(v0 * t_stop))}\\,\\text{{m}}$"
            ]

            # --- BƯỚC 3: LẶP ĐỂ ĐẢM BẢO SỐ CÂU ĐÚNG TỪ 1 ĐẾN 3 ---
            while True:
                ans_a = random.choice(list_da_a)
                ans_b = random.choice(list_da_b)
                ans_c = random.choice(list_da_c)
                ans_d = random.choice(list_da_d)

                shuffled_answers = [ans_a, ans_b, ans_c, ans_d]
                true_count = count_true_answers(shuffled_answers)

                if 1 <= true_count <= 3:
                    break

            # --- BƯỚC 4: XUẤT NỘI DUNG THEO ĐỊNH DẠNG ---
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\choiceTFn \n'
                       '{' + str(shuffled_answers[0]) + '}\n'
                       '{' + str(shuffled_answers[1]) + '}\n'
                       '{' + str(shuffled_answers[2]) + '}\n'
                       '{' + str(shuffled_answers[3]) + '}\n'
                       '\\loigiai{ \n'
                       '\\begin{enumEX}[a)]{1} \n'
                       '\\item ' + str(lg_a) + '\n'
                       '\\item ' + str(lg_b) + '\n'
                       '\\item ' + str(lg_c) + '\n'
                       '\\item ' + str(lg_d) + '\n'
                       '\\end{enumEX}} \n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

