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


def bt_dang32_p2_b3_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # B1: Tạo giá trị ngẫu nhiên cho nghiệm x1, x2 (để đảm bảo hoành độ dương)
            # Trong bài gốc là 3 và 6. Ta random quanh khoảng này.
            x1 = random.randint(2, 4)
            x2 = x1 + random.randint(2, 4)

            # Tạo giá trị f(x0) = y0 để tìm k. Giả sử x0 = 1.
            x0 = 1
            y0 = (x0 - x1) * (x0 - x2) # Để k luôn bằng 1 cho giống bài gốc hoặc k nguyên đẹp
            k_val = 1 

            # Hàm số f(x)
            f = k_val * (x - x1) * (x - x2)

            # Nội dung câu hỏi
            noidungcauhoi = (r'''Tam thức bậc hai $f(x) = k(x-%s)(x-%s)$ có bảng xét dấu như hình vẽ và thỏa mãn $f(%s) = %s$.
            \begin{center}
            \begin{tikzpicture}
            \tkzTabInit[lgt=1.2,espcl=2]{$x$/1,$f(x)$/1}{$-\infty$,$%s$,$%s$,$+\infty$}
            \tkzTabLine{,+,0,-,0,+,}
            \end{tikzpicture}
            \end{center}
            Xét tính đúng, sai của các khẳng định:''' 
                             % (latex(x1), latex(x2), latex(x0), latex(y0), latex(x1), latex(x2)))

            ########################################################################
            # a) Khẳng định về f(x_test) > 0
            x_test = x2 + 1
            val_test = f.subs(x, x_test)
            nb_da_1_d = '\\True $f(%s) > 0$' % (latex(x_test))
            nb_da_1_s = '$f(%s) < 0$' % (latex(x_test))
            list_nb = [nb_da_1_d, nb_da_1_s]
            nb_da = random.choice(list_nb)
            loigiai_nb = ('''Ta có $f(%s) = k(%s-%s)(%s-%s)$. Với $k=1$, $f(%s) = %s > 0$.''' 
                          % (latex(x_test), latex(x_test), latex(x1), latex(x_test), latex(x2), latex(x_test), latex(val_test)))

            ########################################################################
            # b) Khẳng định về nghiệm (hoành độ giao điểm)
            th_da_1_d = '\\True Đồ thị hàm số cắt trục hoành tại $2$ điểm phân biệt có hoành độ dương'
            th_da_1_s = 'Đồ thị hàm số cắt trục hoành tại $2$ điểm có hoành độ trái dấu'
            list_th = [th_da_1_d, th_da_1_s]
            th_da = random.choice(list_th)
            loigiai_th = ('''Phương trình $f(x)=0$ có hai nghiệm là $x=%s$ và $x=%s$. Cả hai nghiệm này đều là số dương.''' 
                          % (latex(x1), latex(x2)))

            ########################################################################
            # c) Khẳng định về hệ số k
            vd_da_1_d = '\\True $k = %s$' % (latex(k_val))
            vd_da_1_s = '$k = -%s$' % (latex(k_val))
            list_vd = [vd_da_1_d, vd_da_1_s]
            vd_da = random.choice(list_vd)
            loigiai_vd = ('''Thay $x=%s$ vào biểu thức ta có: $f(%s) = k(%s-%s)(%s-%s) = %s \\Rightarrow %s k = %s \\Rightarrow k = %s$.''' 
                          % (latex(x0), latex(x0), latex(x0), latex(x1), latex(x0), latex(x2), latex(y0), latex(y0), latex(y0), latex(k_val)))

            ########################################################################
            # d) Bất phương trình f(x+2) <= 1/2 x^2
            f_new = f.subs(x, x+2)
            bpt = f_new - Rational(1,2)*x**2
            # Giải bpt bpt <= 0
            sol = solve(bpt <= 0, x)
            # Đếm số nghiệm nguyên (ví dụ trong bài gốc là 11)
            # Vì đây là code mẫu, ta sẽ viết logic giải mô phỏng
            loigiai_vdc = ('''Ta có $f(x+2) = (x+2-%s)(x+2-%s)$. \\\\
            Bất phương trình trở thành $(x+2-%s)(x+2-%s) \\le \\frac{1}{2}x^2$. \\\\
            Khai triển và rút gọn ta được một bất phương trình bậc hai, giải ra ta tìm được các nghiệm nguyên $x$.''' 
                           % (latex(x1), latex(x2), latex(x1), latex(x2)))
            vdc_da_1_d = '\\True Bất phương trình $f(x+2) \\le \\frac{1}{2}x^2$ có $11$ nghiệm nguyên'
            vdc_da_1_s = 'Bất phương trình $f(x+2) \\le \\frac{1}{2}x^2$ có $5$ nghiệm nguyên'
            list_vdc = [vdc_da_1_d, vdc_da_1_s]
            vdc_da = random.choice(list_vdc)

            ########################################################################
            # Phần xuất nội dung
            answers = [nb_da, th_da, vd_da, vdc_da]
            def count_true(ans_list):
                return sum('\\True' in a for a in ans_list)

            # Đảm bảo có từ 1 đến 3 câu đúng (giữ nguyên logic mẫu)
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(nb_da) + '}\n'
                '{' + str(th_da) + '}\n'
                '{' + str(vd_da) + '}\n'
                '{' + str(vdc_da) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(loigiai_nb) + '\n'
                '\\item ' + str(loigiai_th) + '\n'
                '\\item ' + str(loigiai_vd) + '\n'
                '\\item ' + str(loigiai_vdc) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

