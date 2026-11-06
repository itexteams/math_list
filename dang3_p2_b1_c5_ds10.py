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


def bt_dang3_p2_b1_c5_ds10(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                # Khai báo biến
                a=randint(4,7)
                b=randint(4,7)
                c=randint(3,7)
                while a==b:
                    a=randint(2,9)
                    b=randint(2,6)
                    c=randint(3,7)
                t=a+b+c

                xa=t*(t-1)*(t-2)
                def giaiThua(a):
                    if a == 0:
                        return 1
                    return a * giaiThua(a - 1)
                def giaiThua(b):
                    if b == 0:
                        return 1
                    return b * giaiThua(b - 1)
                def giaiThua(c):
                    if c == 0:
                        return 1
                    return c * giaiThua(c - 1)
                xb=giaiThua(a)
                xb1=giaiThua(b)
                xb2=giaiThua(c)
                xc=xb*xb1*xb2*6
                xd1=(b+c)*(b+c-1)*(b+c-2)
                xd=xa-xd1




                # Nội dung câu hỏi
                noidungcauhoi = ('Có $%s$ sách Toán, $%s$ sách Lý và $%s$ sách Hóa cần xếp trên một giá sách nằm ngang.'
                                %(latex(a),latex(b),latex(c)))



                ######################################################################## Nhận biết ############################################
                # Các đáp án
                nb_da_1_d = '\\True Số cách xếp tùy ý thứ tự các quyển sách là $%s\\cdot %s \\cdot...\\cdot 1$ (cách xếp)'%(latex(t),latex(t-1))
                nb_da_1_s = 'Số cách xếp tùy ý thứ tự các quyển sách là $%s$ (cách xếp)'%(latex(xa))
                list_nb_da_1=[nb_da_1_d,nb_da_1_s]
                nb_da_1=random.choice(list_nb_da_1)

                nb_da_2_d = '\\True Số cách xếp tùy ý thứ tự các quyển sách là $%s\\cdot %s \\cdot...\\cdot 1$ (cách xếp)'%(latex(t),latex(t-1))
                nb_da_2_s = 'Số cách xếp tùy ý thứ tự các quyển sách là $%s\\cdot %s \\cdot...\\cdot 1$ (cách xếp)'%(latex(t-1),latex(t-2))
                list_nb_da_2=[nb_da_2_d,nb_da_2_s]

                nb_da_2=random.choice(list_nb_da_2)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_nb_1 = [nb_da_1, nb_da_2]

                # Nội dung lời giải
                loigiai_nb_1 = ('Tổng có $%s$ quyển sách. Xếp một quyển sách và vị trí thứ nhất của giá có $%s$ (cách xếp).\\\\ \n'
                                'Các vị trí tiếp theo lần lượt có $%s,%s,...,1$ (cách xếp).\\\\ \n'
                                'Vậy có $%s\\cdot %s\\cdot ... \\cdot 1$ cách xếp tùy ý thứ tự các quyển sách.'
                                %(latex(t),latex(t),
                                latex(t-1),latex(t-2),
                                latex(t),latex(t-1),
                                )
                            )
                loigiai_nb_2 = ('Tổng có $%s$ quyển sách. Xếp một quyển sách và vị trí thứ nhất của giá có $%s$ (cách xếp).\\\\ \n'
                                'Các vị trí tiếp theo lần lượt có $%s,%s,...,1$ (cách xếp).\\\\ \n'
                                'Vậy có $%s\\cdot %s\\cdot ... \\cdot 1$ cách xếp tùy ý thứ tự các quyển sách.'
                                %(latex(t),latex(t),
                                latex(t-1),latex(t-2),
                                latex(t),latex(t-1),
                                )
                            )
                # Đưa các lời giải vào danh sách lời giải
                list_nb_2 = [loigiai_nb_1, loigiai_nb_2]

                # Kết hợp các đáp án và lời giải vào cùng một danh sách
                combined_nb = list(zip(list_nb_1, list_nb_2))

                # Xáo trộn danh sách kết hợp
                random.shuffle(combined_nb)

                # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
                shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

                ######################################################################## Thông hiểu ############################################
                # Các đáp án
                th_da_1_d = '\\True Số cách xếp $%s$ quyển Toán cạnh nhau theo hàng là $%s\\cdot %s\\cdot %s \\cdot... \\cdot 1$ (cách xếp)'%(latex(a),latex(xb),latex(b+c+1),latex(b+c),)
                th_da_1_s = 'Số cách xếp $%s$ quyển Toán cạnh nhau theo hàng là $%s$ (cách xếp)'%(latex(a),latex(xb))
                list_th_da_1=[th_da_1_d,th_da_1_s]
                th_da_1=random.choice(list_th_da_1)

                th_da_2_d = '\\True  Số cách xếp $%s$ quyển Lý cạnh nhau theo hàng là $%s\\cdot %s\\cdot %s \\cdot... \\cdot 1$ (cách xếp)'%(latex(b),latex(xb1),latex(a+c+1),latex(a+c),)
                th_da_2_s = 'Số cách xếp $%s$ quyển Lý cạnh nhau theo hàng là $%s$ (cách xếp)'%(latex(b),latex(xb1))
                list_th_da_2=[th_da_2_d,th_da_2_s]

                th_da_2=random.choice(list_th_da_2)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_th_1 = [th_da_1, th_da_2]

                # Nội dung lời giải
                loigiai_th_1 = ('Số cách xếp $%s$ quyển Toán cạnh nhau theo hàng là $%s \\cdot %s \\cdot... \\cdot 1=%s$ (cách xếp).\\\\ \n'
                                'Lúc này ta có $%s$ phần tử xếp lên giá gồm có $X$ cùng với $%s$ sách KHÔNG phải sách Toán (số sách Lý + sách Hóa và $X$ được tính là $1$ phần tử).\\\\ \n'
                                'Số cách chọn phần tử cho các vị trí từ $1$ đến $%s$ lần lượt là $%s,%s,...,1$.\\\\ \n'
                                'Vậy số cách xếp sách thỏa mãn là $%s\\cdot %s\\cdot %s \\cdot... \\cdot 1$.'

                                %(latex(a),latex(a),latex(a-1),latex(xb),
                                latex(b+c+1),latex(b+c), latex(b+c+1),latex(b+c+1),latex(b+c),
                                latex(xb),latex(b+c+1),latex(b+c),
                                )
                            )
                loigiai_th_2 = ('Số cách xếp $%s$ quyển Lý cạnh nhau theo hàng là $%s \\cdot %s \\cdot... \\cdot 1=%s$ (cách xếp).\\\\ \n'
                                'Lúc này ta có $%s$ phần tử xếp lên giá gồm có $X$ cùng với $%s$ sách KHÔNG phải sách Lý (số sách Toán + sách Hóa và $X$ được tính là $1$ phần tử).\\\\ \n'
                                'Số cách chọn phần tử cho các vị trí từ $1$ đến $%s$ lần lượt là $%s,%s,...,1$.\\\\ \n'
                                'Vậy số cách xếp sách thỏa mãn là $%s\\cdot %s\\cdot %s \\cdot... \\cdot 1$.'

                                %(latex(b),latex(b),latex(b-1),latex(xb1),
                                latex(a+c+1),latex(a+c), latex(a+c+1),latex(a+c+1),latex(a+c),
                                latex(xb1),latex(a+c+1),latex(a+c),
                                )
                            )
                # Đưa các lời giải vào danh sách lời giải
                list_th_2 = [loigiai_th_1, loigiai_th_2]

                # Kết hợp các đáp án và lời giải vào cùng một danh sách
                combined_th = list(zip(list_th_1, list_th_2))

                # Xáo trộn danh sách kết hợp
                random.shuffle(combined_th)

                # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
                shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

                ######################################################################## Vận dụng ############################################
                # Các đáp án
                vd_da_1_d = '\\True Số cách xếp sao cho các sách cùng bộ môn nằm cạnh nhau là $%s$ (cách xếp)'%(latex(xc))
                vd_da_1_s = 'Số cách xếp sao cho các sách cùng bộ môn nằm cạnh nhau là $%s$ (cách xếp)'%(latex(xc+2))
                list_vd_da_1=[vd_da_1_d,vd_da_1_s]
                vd_da_1=random.choice(list_vd_da_1)

                vd_da_2_d = '\\True Số cách xếp sao cho các sách cùng bộ môn nằm cạnh nhau là $%s$ (cách xếp)'%(latex(xc))
                vd_da_2_s = 'Số cách xếp sao cho các sách cùng bộ môn nằm cạnh nhau là $%s$ (cách xếp)'%(latex(xc-10))
                list_vd_da_2=[vd_da_2_d,vd_da_2_s]

                vd_da_2=random.choice(list_vd_da_2)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_vd_1 = [vd_da_1, vd_da_2]

                # Nội dung lời giải
                loigiai_vd_1 = ('Số cách xếp $%s$ quyển Toán cạnh nhau theo hàng là $%s \\cdot %s \\cdot... \\cdot 1=%s$ (cách xếp).\\\\ \n'
                                'Số cách xếp $%s$ quyển Lý cạnh nhau theo hàng là $%s \\cdot %s \\cdot... \\cdot 1=%s$ (cách xếp).\\\\ \n'
                                'Số cách xếp $%s$ quyển Hóa cạnh nhau theo hàng là $%s \\cdot %s \\cdot... \\cdot 1=%s$ (cách xếp).\\\\ \n'
                                'Số cách đặt ba nhóm trên (Nhóm sách Toán, nhóm sách Lý, nhóm sách Hóa) theo một hàng ngang là $3\\cdot 2 \\cdot 1=6$ (cách xếp).\\\\ \n'
                                'Vậy có $%s\\cdot %s \\cdot %s\\cdot 6=%s$  cách xếp sao cho các sách cùng bộ môn nằm cạnh nhau.'
                                %(latex(a),latex(a),latex(a-1),latex(xb),
                                latex(b),latex(b),latex(b-1),latex(xb1),
                                latex(c),latex(c),latex(c-1),latex(xb2),
                                latex(xb),latex(xb1),latex(xb2),latex(xc),
                                )
                            )
                loigiai_vd_2 = ('Số cách xếp $%s$ quyển Toán cạnh nhau theo hàng là $%s \\cdot %s \\cdot... \\cdot 1=%s$ (cách xếp).\\\\ \n'
                                'Số cách xếp $%s$ quyển Lý cạnh nhau theo hàng là $%s \\cdot %s \\cdot... \\cdot 1=%s$ (cách xếp).\\\\ \n'
                                'Số cách xếp $%s$ quyển Hóa cạnh nhau theo hàng là $%s \\cdot %s \\cdot... \\cdot 1=%s$ (cách xếp).\\\\ \n'
                                'Số cách đặt ba nhóm trên (Nhóm sách Toán, nhóm sách Lý, nhóm sách Hóa) theo một hàng ngang là $3\\cdot 2 \\cdot 1=6$ (cách xếp).\\\\ \n'
                                'Vậy có $%s\\cdot %s \\cdot %s\\cdot 6=%s$  cách xếp sao cho các sách cùng bộ môn nằm cạnh nhau.'
                                %(latex(a),latex(a),latex(a-1),latex(xb),
                                latex(b),latex(b),latex(b-1),latex(xb1),
                                latex(c),latex(c),latex(c-1),latex(xb2),
                                latex(xb),latex(xb1),latex(xb2),latex(xc),
                                )
                            )

                # Đưa các lời giải vào danh sách lời giải
                list_vd_2 = [loigiai_vd_1, loigiai_vd_2]

                # Kết hợp các đáp án và lời giải vào cùng một danh sách
                combined_vd = list(zip(list_vd_1, list_vd_2))

                # Xáo trộn danh sách kết hợp
                random.shuffle(combined_vd)

                # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
                shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

                ######################################################################## Vận dụng cao ############################################
                # Các đáp án
                vdc_da_1_d = '\\True Số cách xếp sao cho hai quyển Toán mỗi quyển nằm ở một đầu giá sách là $%s\\cdot %s\\cdot%s\\cdot... \\cdot 1$ (cách xếp)'%(latex(a*(a-1)),latex(t-2),latex(t-3))
                vdc_da_1_s = 'Số cách xếp sao cho hai quyển Toán mỗi quyển nằm ở một đầu giá sách là $%s\\cdot %s\\cdot%s\\cdot... \\cdot 1$ (cách xếp)'%(latex(a),latex(t-2),latex(t-3))
                list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
                vdc_da_1=random.choice(list_vdc_da_1)

                vdc_da_2_d = '\\True Số cách xếp sao cho hai quyển Lý mỗi quyển nằm ở một đầu giá sách là $%s\\cdot %s\\cdot%s\\cdot... \\cdot 1$ (cách xếp)'%(latex(c*(c-1)),latex(t-2),latex(t-3))
                vdc_da_2_s = 'Số cách xếp sao cho hai quyển Lý mỗi quyển nằm ở một đầu giá sách là $%s\\cdot%s\\cdot... \\cdot 1$ (cách xếp)'%(latex(t-2),latex(t-3))
                list_vdc_da_2=[vdc_da_2_d,vdc_da_2_s]

                vdc_da_2=random.choice(list_vdc_da_2)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_vdc_1 = [vdc_da_1, vdc_da_2]

                # Nội dung lời giải
                loigiai_vdc_1 = ('Số cách xếp $1$ quyển Toán ở đầu giá sách có $%s$ (cách xếp).\\\\ \n'
                                'Số cách xếp $1$ quyển Toán ở cuối giá sách có $%s$ (cách xếp).\\\\ \n'
                                'Còn lại $%s$ quyển sách có $%s\\cdot %s \\cdot... \\cdot 1$ (cách xếp)\\\\ \n'
                                'Vậy có $%s\\cdot %s\\cdot %s\\cdot %s\\cdot... \\cdot 1= %s\\cdot %s\\cdot %s\\cdot... \\cdot 1$ cách xếp thỏa mãn yêu cầu.'
                                %(
                                    latex(a),
                                    latex(a-1),
                                latex(t-2),latex(t-2),latex(t-3),
                                latex(a),latex(a-1),latex(t-2),latex(t-3), latex(a*(a-1)),latex(t-2),latex(t-3),

                                )
                            )
                loigiai_vdc_2 = ('Số cách xếp $1$ quyển Lý ở đầu giá sách có $%s$ (cách xếp).\\\\ \n'
                                'Số cách xếp $1$ quyển Lý ở cuối giá sách có $%s$ (cách xếp).\\\\ \n'
                                'Còn lại $%s$ quyển sách có $%s\\cdot %s \\cdot... \\cdot 1$ (cách xếp)\\\\ \n'
                                'Vậy có $%s\\cdot %s\\cdot %s\\cdot %s\\cdot... \\cdot 1= %s\\cdot %s\\cdot %s\\cdot... \\cdot 1$ cách xếp thỏa mãn yêu cầu.'
                                %(
                                    latex(c),
                                    latex(c-1),
                                latex(t-2),latex(t-2),latex(t-3),
                                latex(c),latex(c-1),latex(t-2),latex(t-3), latex(c*(c-1)),latex(t-2),latex(t-3),

                                )
                            )
                # Đưa các lời giải vào danh sách lời giải
                list_vdc_2 = [loigiai_vdc_1, loigiai_vdc_2]

                # Kết hợp các đáp án và lời giải vào cùng một danh sách
                combined_vdc = list(zip(list_vdc_1, list_vdc_2))

                # Xáo trộn danh sách kết hợp
                random.shuffle(combined_vdc)

                # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
                shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)



            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
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
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content

