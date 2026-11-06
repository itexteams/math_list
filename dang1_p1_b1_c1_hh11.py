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


def bt_dang1_p1_b1_c1_hh11(self):
            # Khai báo biến
            lisdang=['1','2','3','4','5','6','7','8','9','10','11','12','13']
            dang=random.choice(lisdang)
            if dang=='13':
                # Khai báo biến                   
                du = ['chúng có một đường thẳng chung duy nhất',
                    ]
                da= random.choice(du)
                s = ['chúng có một tam giác chung',
                    'chúng không có thêm điểm chung nhào khác nữa',
                    'chúng có một đoạn thẳng chung',
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('''Trong không gian. Hai mặt phẳng phân biệt có một điểm chung thì'''
                                %(
                                ))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('''Trong không gian. Hai mặt phẳng phân biệt có một điểm chung thì chúng có một đường thẳng chung duy nhất.'''
                        %(
                        ))                 
            if dang=='12':
                # Khai báo biến                   
                du = ['Cùng thuộc đường thẳng',
                    ]
                da= random.choice(du)
                s = ['Cùng thuộc mặt cầu',
                    'Cùng thuộc đường tròn',
                    'Cùng thuộc đường elip',
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Trong không gian. Ba điểm phân biệt cùng thuộc hai mặt phẳng phân biệt thì \n'
                                %(
                                ))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('''Qua ba điểm phân biệt không thẳng hàng thì chỉ xác định được một và chỉ một mặt phẳng. Ở đây thuộc hai mặt phẳng phân biệt nên ít nhất một trong hai điều kiện phân biệt hoặc thẳng hàng không thỏa mãn. Mà ba điểm đề cho đã phân biệt nên chúng phải thẳng hàng.'''
                        %(
                        ))                 
            if dang=='11':
                # Khai báo biến                   
                du = ['Điểm có thể thuộc mặt phẳng, có thể không thuộc mặt phẳng',
                    ]
                da= random.choice(du)
                s = ['Điểm luôn phải thuộc mặt phẳng',
                    'Điểm luôn luôn không thuộc mặt phẳng',
                    'Điểm vừa thuộc mặt phẳng đồng thời vừa không thuộc mặt phẳng',
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Trong không gian, khẳng định nào sau đây đúng? \n'
                                %(
                                ))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Điểm có thể thuộc mặt phẳng, có thể không thuộc mặt phẳng.'
                        %(
                        ))           
            if dang=='10':
                # Khai báo biến
                lisdiem=['A','B','C','D','M','N','I','H','K']
                diem=random.choice(lisdiem)
                lismp=['P','Q','R','\\alpha','\\beta']
                mp=random.choice(lismp)

                du = ['$3$',
                    ]
                da= random.choice(du)
                s = ['$1$',
                    '$2$',
                    '$4$',
                    '$0$',
                    '$5$',
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Trong không gian, có bao nhiêu cách xác định một mặt phẳng? \n'
                                %(
                                ))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Trong không gian, một mặt phẳng hoàn toàn được xác định khi \\\\ \n'
                        '\\hspace*{1cm} Đi qua ba điểm không thẳng hàng.'
                        '\\hspace*{1cm} Đi qua một điểm và chứa một đường thẳng không đi qua điểm đó.'
                        '\\hspace*{1cm} Chứa hai đường thẳng cắt nhau.'
                        %(
                        ))
            if dang=='9':
                # Khai báo biến
                lisdiem=['a','b','c','d']
                diem=random.choice(lisdiem)
                lismp=['P','Q','R','\\alpha','\\beta']
                mp=random.choice(lismp)

                du = ['$%s \\subset (%s)$'%(str(diem),str(mp)),
                    ]
                da= random.choice(du)
                s = ['$%s \\in (%s)$'%(str(diem),str(mp)),
                    '$%s \\notin (%s)$'%(str(diem),str(mp)),
                    '$%s < (%s)$'%(str(diem),str(mp)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Trong không gian, đường thẳng $%s$ nằm trong mặt phẳng $(%s)$ được ký hiệu là \n'
                                %(str(diem),str(mp)
                                ))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Trong không gian, đường thẳng $%s$ nằm trong mặt phẳng $(%s)$ được ký hiệu là $%s \\subset (%s)$.\\\\ \n'
                        %(str(diem),str(mp),str(diem),str(mp)
                        ))
            if dang=='8':
                # Khai báo biến
                lisdiem=['A','B','C','D','M','N','I','H','K']
                diem=random.choice(lisdiem)
                lismp=['P','Q','R','\\alpha','\\beta']
                mp=random.choice(lismp)

                du = ['Có hai đường thẳng phân biệt cùng đi qua hai điểm phân biệt cho trước',
                    ]
                da= random.choice(du)
                s = ['Tồn tại bốn điểm không cùng thuộc một mặt phẳng',
                    'Có một và chỉ một mặt phẳng đi qua ba điểm không thẳng hàng',
                    'Nếu một đường thẳng đi qua hai điểm phân biệt thuộc một mặt phẳng thì mọi điểm của đường thẳng đều thuộc mặt phẳng đó',
                    'Có một và chỉ một đường thẳng đi qua hai điểm phân biệt',
                    'Nếu hai mặt phẳng phân biệt có điểm chung thì các điểm chung của hai mặt phẳng là một đường thẳng đi qua hai điểm chung đó',
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Trong không gian, khẳng định nào sau đây là \\textbf{sai}? \n'
                                %(
                                ))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Khẳng định sai là \\\\ \n'
                        '\\hspace*{1cm} Có hai đường thẳng phân biệt cùng đi qua hai điểm phân biệt cho trước.'
                        %(
                        ))
            if dang=='7':
                # Khai báo biến
                lisdiem=['A','B','C','D','M','N','I','H','K']
                diem=random.choice(lisdiem)
                lismp=['P','Q','R','\\alpha','\\beta']
                mp=random.choice(lismp)

                du = ['ba điểm không thẳng hàng',
                    ]
                da= random.choice(du)
                s = ['một đường thẳng và một điểm thuộc nó',
                    'ba điểm mà nó đi qua',
                    'hai đường thẳng thuộc mặt phẳng',
                    'hai điểm phân biệt',
                    'hai đường thẳng trùng nhau',
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Trong không gian, một mặt phẳng hoàn toàn được xác định khi biết \n'
                                %(
                                ))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Trong không gian, một mặt phẳng hoàn toàn được xác định khi biết ba điểm không thẳng hàng.\\\\ \n'
                        %(
                        ))

            if dang=='6':
                # Khai báo biến
                lisdiem=['A','B','C','D','M','N','I','H','K']
                diem=random.choice(lisdiem)
                lismp=['P','Q','R','\\alpha','\\beta']
                mp=random.choice(lismp)

                du = ['hai đường thẳng cắt nhau',
                    ]
                da= random.choice(du)
                s = ['hai đường thẳng song song',
                    'hai đường thẳng trùng nhau',
                    'hai đường thẳng chéo nhau',
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Trong không gian, hình biểu diễn của hai đường thẳng cắt nhau là \n'
                                %(
                                ))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Trong không gian, hình biểu diễn của hai đường thẳng cắt nhau là hai đường thẳng cắt nhau.\\\\ \n'
                        %(
                        ))

            if dang=='5':
                # Khai báo biến
                lisdiem=['A','B','C','D','M','N','I','H','K']
                diem=random.choice(lisdiem)
                lismp=['P','Q','R','\\alpha','\\beta']
                mp=random.choice(lismp)

                du = ['hai đường thẳng song song',
                    ]
                da= random.choice(du)
                s = ['hai đường thẳng cắt nhau',
                    'hai đường thẳng trùng nhau',
                    'hai đường thẳng chéo nhau',
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Trong không gian, hình biểu diễn của hai đường thẳng song song là \n'
                                %(
                                ))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Trong không gian, hình biểu diễn của hai đường thẳng song song là hai đường thẳng song song.\\\\ \n'
                        %(
                        ))

            if dang=='4':
                # Khai báo biến
                lisdiem=['A','B','C','D','M','N','I','H','K']
                diem=random.choice(lisdiem)
                lismp=['P','Q','R','\\alpha','\\beta']
                mp=random.choice(lismp)

                du = ['đoạn thẳng',
                    ]
                da= random.choice(du)
                s = ['đường thẳng',
                    'đường tròn',
                    'mặt phẳng',
                    'một điểm',
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Trong không gian, hình biểu diễn của đoạn thẳng là \n'
                                %(
                                ))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Trong không gian, hình biểu diễn của đoạn thẳng là đoạn thẳng.\\\\ \n'
                        %(
                        ))

            if dang=='3':
                # Khai báo biến
                lisdiem=['A','B','C','D','M','N','I','H','K']
                diem=random.choice(lisdiem)
                lismp=['P','Q','R','\\alpha','\\beta']
                mp=random.choice(lismp)

                du = ['đường thẳng',
                    ]
                da= random.choice(du)
                s = ['đoạn thẳng',
                    'đường tròn',
                    'mặt phẳng',
                    'một điểm',
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Trong không gian, hình biểu diễn của đường thẳng là \n'
                                %(
                                ))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Trong không gian, hình biểu diễn của đường thẳng là đường thẳng.\\\\ \n'
                        %(
                        ))
            if dang=='2':
                # Khai báo biến
                lisdiem=['A','B','C','D','M','N','I','H','K']
                diem=random.choice(lisdiem)
                lismp=['P','Q','R','\\alpha','\\beta']
                mp=random.choice(lismp)

                du = ['$%s \\notin (%s)$'%(str(diem),str(mp)),
                    ]
                da= random.choice(du)
                s = ['$%s \\subset (%s)$'%(str(diem),str(mp)),
                    '$%s \\in (%s)$'%(str(diem),str(mp)),
                    '$%s < (%s)$'%(str(diem),str(mp)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Trong không gian, điểm $%s$ không thuộc mặt phẳng $(%s)$ được ký hiệu là \n'
                                %(str(diem),str(mp)
                                ))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Trong không gian, điểm $%s$ không thuộc mặt phẳng $(%s)$ được ký hiệu là $%s \\notin (%s)$.\\\\ \n'
                        %(str(diem),str(mp),str(diem),str(mp)
                        ))

            if dang=='1':
                # Khai báo biến
                lisdiem=['A','B','C','D','M','N','I','H','K']
                diem=random.choice(lisdiem)
                lismp=['P','Q','R','\\alpha','\\beta']
                mp=random.choice(lismp)

                du = ['$%s \\in (%s)$'%(str(diem),str(mp)),
                    ]
                da= random.choice(du)
                s = ['$%s \\subset (%s)$'%(str(diem),str(mp)),
                    '$%s \\notin (%s)$'%(str(diem),str(mp)),
                    '$%s < (%s)$'%(str(diem),str(mp)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Trong không gian, điểm $%s$ thuộc mặt phẳng $(%s)$ được ký hiệu là \n'
                                %(str(diem),str(mp)
                                ))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Trong không gian, điểm $%s$ thuộc mặt phẳng $(%s)$ được ký hiệu là $%s \\in (%s)$.\\\\ \n'
                        %(str(diem),str(mp),str(diem),str(mp)
                        ))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content

