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


def bt_dang7_p3_b2_c5_ds10(self):
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Dùng vòng lặp để đảm bảo kq_val < 9999
                while True:
                    # Giới hạn n trong khoảng 4 đến 6 để xác suất thỏa mãn điều kiện cao hơn
                    n = random.randint(4, 6)
                    k = 2 
                    m = n - k

                    # Công thức số dãy đẹp của máng m: S(m) = (m+1)^(m-1)
                    sm = (m + 1)**(m - 1)

                    # Tính A_n^k
                    ank = sp.factorial(n) // sp.factorial(n - k)

                    # Kết quả cuối cùng
                    kq_val = ank * sm

                    # Kiểm tra điều kiện: Nếu thỏa mãn thì thoát vòng lặp
                    if kq_val < 9999:
                        break

                da = '$%s$' % (latex(kq_val))

                # Tạo các đáp án sai
                s = [
                    '$%s$' % (latex(kq_val + 20)),
                    '$%s$' % (latex(kq_val - 20)),
                    '$%s$' % (latex(ank * (m**m))), 
                    '$%s$' % (latex(sp.factorial(n) // sp.factorial(n - k + 1) * sm)),
                    '$%s$' % (latex(kq_val + 50)),
                    '$%s$' % (latex(kq_val + 100))
                ]

                s = list(set([x for x in s if x != da and "-" not in x])) # Loại bỏ đáp án âm
                random.shuffle(s)

                das1, das2, das3 = s[:3]

                # Câu hỏi
                list_fixed_diameters = [n - i for i in range(k)]
                str_fixed = " và ".join(["một quả có đường kính là %s" % (latex(d)) for d in list_fixed_diameters])

                # (Phần hinhve giữ nguyên như cũ của bạn)
                hinhve = r'''...''' # [Giữ nguyên code TikZ của bạn ở đây]

                noidungcauhoi = (r'''Hệ thống gồm các vật như sau gọi là \textbf{máng n} \\
                                 - Một máng nghiêng có $n$ lỗ dọc theo đáy. Tính từ trên cao xuống, các lỗ lần lượt có đường kính là $1, 2, 3, ...,n$. \\
                                 - $n$ quả bóng có đường kính là các số nguyên dương không lớn hơn $n$, trong đó có thể có nhiều quả bóng có cùng đường kính.\\
                                 (Hình vẽ dưới đây mô tả \textbf{máng 4}) %s
                                 Xét máng $%s$, thả lăn $%s$ quả bóng từ đỉnh máng xuống, lần lượt từng quả. Đối với mỗi quả bóng, khi lăn đến lỗ có đường kính lớn hơn hoặc bằng đường kính của nó thì nó sẽ lọt vào đồng thời đóng lỗ này lại. Đối với một thứ tự các quả bóng sau khi thả lăn, nếu các quả bóng đều lọt vào lỗ thì thứ tự các quả bóng ấy được gọi là \textbf{dãy đẹp}.
                                 Hai \textbf{dãy đẹp} giống nhau khi và chỉ khi thứ tự bán kính của bóng lọt lỗ là như nhau. 
                                 Có thể tạo được bao nhiêu \textbf{dãy đẹp} khác nhau đối với máng $%s$ biết rằng có đúng %s? '''
                                  % (hinhve, latex(n), latex(n),  latex(n), str_fixed ))

                # Nội dung lời giải
                loigiai = ('''Theo lý thuyết về bài toán máng $n$, số dãy đẹp của một máng $m$ bất kỳ (với các quả bóng có đường kính không vượt quá $m$) được tính theo công thức $S\\left( m \\right) = \\left( m+1 \\right)^{m-1}$.\\\\
                            Bằng cách liệt kê hoặc sử dụng công thức, ta có số dãy đẹp của máng $%s$ là $%s$.\\\\
                            Trong máng $%s$, ta có $%s$ quả bóng có đường kính cố định là $ %s $. Số cách chọn ra $%s$ lượt thứ tự trong tổng số $%s$ lượt để thả các quả bóng này là $A_{%s}^{%s} = %s$.\\\\
                            Với mỗi cách chọn vị trí cho $%s$ quả bóng lớn, có $%s$ cách sắp xếp các quả bóng còn lại vào các lỗ còn lại để tạo thành dãy đẹp.\\\\
                            Vậy số dãy đẹp của máng $%s$ thỏa mãn yêu cầu bài toán là $A_{%s}^{%s} \\times %s = %s$.'''
                           %(latex(m), latex(sm),
                             latex(n), latex(k), " \\, \\text{và} \\,".join([str(d) for d in list_fixed_diameters]), latex(k), latex(n), latex(n), latex(k), latex(ank),
                             latex(k), latex(sm),
                             latex(n), latex(n), latex(k), latex(sm), latex(kq_val)
                            ))
                dapan='\\shortans[0]{$%s$}\n'%(latex(kq_val))

            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

